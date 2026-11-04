"""Validate items.csv and produce summary tables and a chart.

Usage:  python script.py [path/to/items.csv]
Outputs (written next to the CSV): summary_framing_by_purpose.csv, chart_framing_by_purpose.png
"""
import sys
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("items.csv")
df = pd.read_csv(path, dtype=str, keep_default_na=False)

REQUIRED = ["item_id", "source_id", "institution", "source_type", "source_title", "publication_date", "url",
            "access_date", "passage_paraphrase", "stated_purpose", "boundary_framing", "boundary_rule",
            "imagined_audience", "evidence_cited", "responsibility_frame", "interpretation_note"]
ALLOWED = {
    "source_type": {"academic_support_advice", "institutional_news_advice", "campus_publication", "career_services",
                    "counseling_wellness", "platform_feature", "news_coverage"},
    "stated_purpose": {"study_focus", "procrastination", "wellbeing", "news_following", "professional_networking",
                       "community_belonging"},
    "boundary_framing": {"distracting", "productive", "conditional"},
    "evidence_cited": {"none", "anecdote", "staff_expertise", "interviewee_opinion", "statistic_unsourced",
                       "statistic_sourced", "research_unnamed", "research_named"},
    "responsibility_frame": {"individual", "shared", "institutional", "platform_design", "unstated"},
}

problems = []

# 1. required columns and blanks
missing_cols = [c for c in REQUIRED if c not in df.columns]
if missing_cols:
    problems.append(f"Missing columns: {missing_cols}")
for c in [c for c in REQUIRED if c in df.columns]:
    blanks = df.index[df[c].str.strip() == ""].tolist()
    if blanks:
        problems.append(f"Blank values in '{c}' at rows {[b + 2 for b in blanks]} (CSV line numbers)")

# 2. controlled vocabularies (check both the draft label and your reviewed label)
for c, ok in ALLOWED.items():
    bad = df[~df[c].isin(ok)]
    if len(bad):
        problems.append(f"Unexpected values in '{c}': {sorted(bad[c].unique())} (items {bad['item_id'].tolist()})")
if "reviewer_boundary_framing" in df.columns:
    rb = df[(df["reviewer_boundary_framing"] != "") & (~df["reviewer_boundary_framing"].isin(ALLOWED["boundary_framing"]))]
    if len(rb):
        problems.append(f"Unexpected reviewer_boundary_framing values in items {rb['item_id'].tolist()}")

# 3. identifiers and duplicates
if df["item_id"].duplicated().any():
    problems.append(f"Duplicate item_id: {df.loc[df['item_id'].duplicated(), 'item_id'].tolist()}")
if df["passage_paraphrase"].duplicated().any():
    problems.append("Duplicate passages found")
bad_url = df[~df["url"].str.startswith(("http://", "https://"))]
if len(bad_url):
    problems.append(f"Non-URL values in url: {bad_url['item_id'].tolist()}")

# 4. paraphrase hygiene: flag quotation marks and very long passages
quoted = df[df["passage_paraphrase"].str.contains('["\u201c\u201d]', regex=True)]
if len(quoted):
    problems.append(f"Passages containing quotation marks (should be paraphrase): {quoted['item_id'].tolist()}")
long_ = df[df["passage_paraphrase"].str.len() > 400]
if len(long_):
    problems.append(f"Passages longer than 400 characters: {long_['item_id'].tolist()}")

# 5. report
print(f"Rows: {len(df)}   Sources: {df['source_id'].nunique()}   Institutions: {df['institution'].nunique()}")
print(f"Items with unknown publication date: {(df['publication_date'] == 'unknown').sum()}")
print("\nProblems found:" if problems else "\nNo validation problems found.")
for p in problems:
    print(" -", p)

print("\nItems per source type:")
print(df["source_type"].value_counts().to_string())
print("\nBoundary framing overall:")
print(df["boundary_framing"].value_counts().to_string())

ct = pd.crosstab(df["stated_purpose"], df["boundary_framing"])
for col in ["distracting", "conditional", "productive"]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[["distracting", "conditional", "productive"]]
print("\nBoundary framing by stated purpose:")
print(ct.to_string())
ct.to_csv(path.with_name("summary_framing_by_purpose.csv"))

print("\nEvidence cited by boundary framing:")
print(pd.crosstab(df["evidence_cited"], df["boundary_framing"]).to_string())
print("\nResponsibility frame by boundary framing:")
print(pd.crosstab(df["responsibility_frame"], df["boundary_framing"]).to_string())

# 6. chart
order = ct.sum(axis=1).sort_values().index
ct = ct.loc[order]
fig, ax = plt.subplots(figsize=(8, 4.5))
colors = {"distracting": "#B5483A", "conditional": "#C9A227", "productive": "#3E7C59"}
left = pd.Series(0, index=ct.index)
for col in ct.columns:
    ax.barh(ct.index, ct[col], left=left, label=col, color=colors[col])
    left += ct[col]
ax.set_xlabel("Number of passages")
ax.set_title("How advice frames social media, by stated purpose of use")
ax.legend(title="Boundary framing", frameon=False)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.savefig(path.with_name("chart_framing_by_purpose.png"), dpi=160)
print("\nWrote summary_framing_by_purpose.csv and chart_framing_by_purpose.png")
