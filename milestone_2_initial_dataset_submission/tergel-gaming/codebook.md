# Codebook: How U.S. colleges and campus media frame gaming and academics

One row = one passage (a recommendation, claim, or example) from a public page, stored as a paraphrase. Several rows can come from one source (same `source_id`). Label what the passage says, not what you think the writer believes.

| Field | Values | Rule of thumb |
|---|---|---|
| `gaming_role` | stress_relief, community_belonging, leisure, distraction, addiction_problem, academic_support, competition_esports, other | The one purpose the passage emphasizes most. Record a second purpose in `secondary_role` (same values, optional). |
| `academic_framing` | harmful, neutral, beneficial, conditional, mixed, not_stated | Use `neutral` for an explicit claim of no academic effect. Use `not_stated` when the passage gives no academic effect or academic boundary. Use `mixed` for competing academic claims without an explicit condition. Use `conditional` when the passage gives an academic condition and record it in `framing_rule`. |
| `framing_rule` | free text | The condition or line the passage draws (time, intention, amount, signs of a problem), or "none stated". |
| `imagined_audience` | free text | Who the passage seems written for (students, parents, advisors, incoming students). |
| `evidence_cited` | none, anecdote, staff_expertise, interviewee_opinion, statistic_unsourced, statistic_sourced, research_unnamed, research_named, expert_attribution | Use `expert_attribution` for a claim attributed to an outside specialist without a named study. Otherwise, code what backs the claim in the passage itself. Note when several outlets rely on the same study. |
| `responsibility_frame` | individual, shared, institutional, platform_design, unstated | Who is asked or expected to act. |
| `source_type` | campus_publication, institutional_news, counseling_wellness, academic_support_advice, advising_professional, national_news, parent_facing_media, esports_org | The kind of outlet, not the topic. |
| `us_context` | stated, inferred | Whether the page says it is about a U.S. school or you inferred it. |
| `verified` | yes, no | `yes` only after the student reads the full page and checks the paraphrase and every label. An AI source check is recorded in the separate review log. |
| `interpretation_note` | free text | Why a label was hard, or what the categories flatten. |

Other rules
- Paraphrase only. No direct quotes, no student names.
- `publication_date`: YYYY, YYYY-MM, YYYY-MM-DD, or `unknown`.
- Exclude: non-U.S. outlets, commercial or SEO pages with no clear author, pages you cannot open, and passages that mention gaming only in passing.