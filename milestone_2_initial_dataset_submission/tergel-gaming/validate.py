
import re
import sys
from datetime import date
from pathlib import Path

import pandas as pd

COLUMNS = [
    "item_id", "source_id", "institution", "source_type", "source_title",
    "publication_date", "url", "access_date", "passage_paraphrase",
    "gaming_role", "secondary_role", "academic_framing", "framing_rule",
    "imagined_audience", "evidence_cited", "responsibility_frame",
    "us_context", "verified", "interpretation_note",
]

ROLES = ["stress_relief", "community_belonging", "leisure", "distraction",
         "addiction_problem", "academic_support", "competition_esports", "other"]

VOCAB = {
    "source_type": ["campus_publication", "institutional_news", "counseling_wellness",
                    "academic_support_advice", "advising_professional",
                    "national_news", "parent_facing_media", "esports_org"],
    "gaming_role": ROLES,
    "academic_framing": ["harmful", "neutral", "beneficial", "conditional", "mixed", "not_stated"],
    "evidence_cited": ["none", "anecdote", "staff_expertise", "interviewee_opinion",
                       "statistic_unsourced", "statistic_sourced",
                       "research_unnamed", "research_named", "expert_attribution"],
    "responsibility_frame": ["individual", "shared", "institutional",
                             "platform_design", "unstated"],
    "us_context": ["stated", "inferred"],
    "verified": ["yes", "no"],
}
OPTIONAL_VOCAB = {"secondary_role": ROLES}

REQUIRED_TEXT = ["item_id", "source_id", "institution", "source_title", "url",
                 "access_date", "passage_paraphrase", "framing_rule",
                 "imagined_audience"]
SOURCE_CONSISTENT = ["institution", "source_type", "source_title", "url",
                     "publication_date"]

DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
QUOTE_CHARS = ['"', "\u201c", "\u201d"]


def valid_date(value, allow_unknown):
    if allow_unknown and value == "unknown":
        return True
    if not DATE_RE.match(value):
        return False
    parts = [int(p) for p in value.split("-")]
    try:
        date(parts[0], parts[1] if len(parts) > 1 else 1,
             parts[2] if len(parts) > 2 else 1)
    except ValueError:
        return False
    return True


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    path = Path(args[0] if args else "items.csv")
    out_dir = path.parent

    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    errors, warnings = [], []

    missing = [c for c in COLUMNS if c not in df.columns]
    extra = [c for c in df.columns if c not in COLUMNS]
    if missing:
        errors.append(f"Missing columns: {missing}")
    if extra:
        warnings.append(f"Unexpected columns (ignored): {extra}")
    if missing:
        report(df, errors, warnings)
        sys.exit(1)

    for i, row in df.iterrows():
        rid = row["item_id"] or f"row {i + 2}"
        for col in REQUIRED_TEXT:
            if not row[col].strip():
                errors.append(f"{rid}: '{col}' is empty")
        for col, allowed in VOCAB.items():
            if row[col] not in allowed:
                errors.append(f"{rid}: {col}='{row[col]}' not in {allowed}")
        for col, allowed in OPTIONAL_VOCAB.items():
            if row[col] and row[col] not in allowed:
                errors.append(f"{rid}: {col}='{row[col]}' not in {allowed}")
        if row["secondary_role"] and row["secondary_role"] == row["gaming_role"]:
            errors.append(f"{rid}: secondary_role repeats gaming_role")
        if not valid_date(row["publication_date"], allow_unknown=True):
            errors.append(f"{rid}: publication_date '{row['publication_date']}' "
                          "must be YYYY, YYYY-MM, YYYY-MM-DD, or 'unknown'")
        if not valid_date(row["access_date"], allow_unknown=False):
            errors.append(f"{rid}: access_date '{row['access_date']}' is not a valid date")
        if not row["url"].startswith(("http://", "https://")):
            errors.append(f"{rid}: url does not start with http(s)://")
        text = row["passage_paraphrase"]
        if any(q in text for q in QUOTE_CHARS):
            errors.append(f"{rid}: paraphrase contains quotation marks "
                          "(paraphrase only, no direct quotes)")
        words = len(text.split())
        if text and words < 8:
            warnings.append(f"{rid}: paraphrase is very short ({words} words)")
        if words > 70:
            warnings.append(f"{rid}: paraphrase is long ({words} words); "
                            "is it close to the source wording?")

    for col, label in [("item_id", "item_id"), ("passage_paraphrase", "paraphrase")]:
        dup = df[df.duplicated(col, keep=False) & (df[col] != "")]
        for value in dup[col].unique():
            ids = ", ".join(dup[dup[col] == value]["item_id"])
            errors.append(f"Duplicate {label} in rows: {ids}")

    for sid, group in df.groupby("source_id"):
        for col in SOURCE_CONSISTENT:
            if group[col].nunique() > 1:
                ids = ", ".join(group["item_id"])
                errors.append(f"Source {sid}: '{col}' differs across rows ({ids})")

    unverified = (df["verified"] != "yes").sum()
    if unverified:
        msg = f"{unverified} of {len(df)} rows are not verified yet (verified != 'yes')"
        (errors if strict else warnings).append(msg)

    report(df, errors, warnings)
    summarize(df, out_dir, chart="--no-chart" not in sys.argv)
    sys.exit(1 if errors else 0)


def report(df, errors, warnings):
    print(f"Rows: {len(df)}")
    print(f"Sources: {df['source_id'].nunique() if 'source_id' in df else 'n/a'}")
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print("RESULT:", "FAILED" if errors else "OK",
          f"({len(errors)} errors, {len(warnings)} warnings)")


def summarize(df, out_dir, chart=True):
    role_by_frame = pd.crosstab(df["gaming_role"], df["academic_framing"])
    role_by_frame.to_csv(out_dir / "summary_role_by_framing.csv")
    pd.crosstab(df["source_type"], df["gaming_role"]).to_csv(
        out_dir / "summary_source_by_role.csv")
    print("\nGaming role x academic framing (counts):")
    print(role_by_frame.to_string())

    if not chart:
        return

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    ax = role_by_frame.plot(kind="bar", stacked=True, figsize=(8, 5))
    ax.set_xlabel("Stated gaming role")
    ax.set_ylabel("Passages")
    ax.set_title("How passages frame gaming's effect on academics, by role\n"
                 "(sample reflects search design, not prevalence)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / "chart_role_by_framing.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
