# Milestone 2 — Gaming and academic life in U.S. college discourse

## Research question

How do public sources about U.S. colleges frame video gaming in relation to academic life, and who do they expect to act when gaming is presented as a problem? I use public campus reporting, university news, wellness guidance, and selected national and parent-facing media. These sources let me study what institutions, writers, and speakers consider productive, distracting, or supportive. The passage is the unit of analysis.

## Dataset and selection

The initial dataset contains **43 passages from 19 sources**. I included passages that substantively discuss gaming in a U.S. college context. I kept passages about campus belonging and stress relief because they show how sources place gaming in college life, including when they leave its academic consequences unstated. I excluded I009 because its passage covers general counseling and academic stress without discussing gaming. Seven other candidates are pending because their full articles could not be retrieved. To reach at least 50 passages, I plan to look for archived copies of the seven articles and replace any inaccessible items with passages that meet the same criteria.

The data are in UTF-8 CSV because the passages have a consistent set of fields and can be read directly with Python. `item_id` identifies a passage and `source_id` groups passages from the same publication. The provenance fields are `institution`, `source_type`, `source_title`, `publication_date`, `url`, `access_date`, and `us_context`. An unknown publication date is recorded as `unknown`. `passage_paraphrase` holds the working representation. `gaming_role` and optional `secondary_role` capture the purposes attributed to play. `academic_framing` and `framing_rule` record the academic evaluation and any stated boundary. `imagined_audience`, `evidence_cited`, and `responsibility_frame` track who is addressed, what supports the claim, and who is expected to act. `interpretation_note` records the location and coding rationale. The codebook gives the complete field definitions.

## Two transformations

1. **Public text to working representation.** Each selected passage becomes a short paraphrase with a source URL and a locator in the article. For example, I005 condenses a student editorial’s closing advice about when to play. I omit student names and direct quotations. [Lehigh editorial](https://thebrownandwhite.com/2024/12/03/beyond-the-screen-and-controller/)
2. **Working representation to structured record.** I005 codes the role as `leisure`, the academic framing as `conditional`, and responsibility as `individual`. The rule records the proposed timing boundary. I007 uses `not_stated` for academic framing because the speaker discusses relief from stress and connection with other students without evaluating schoolwork. `neutral` is reserved for an explicit claim of no academic effect. [Reporting Texas article](https://www.reportingtexas.com/students-turn-to-gaming-for-relief-from-midterm-stress/)

## Computation and review

`validate.py` checks required fields, category values, dates, duplicate IDs and paraphrases, and consistency across rows with the same source ID. Run the commands below from the `tergel-gaming` folder to reproduce the two summary tables and the chart. The script saves all three outputs beside `items.csv`.

```bash
python -m pip install pandas matplotlib
python validate.py items.csv
```

The script uses pandas to count each passage under its primary gaming role. `summary_role_by_framing.csv` shows how often each role appears with each academic framing. For example, nine of the 11 passages coded as `community_belonging` leave the academic effect unstated. `chart_role_by_framing.png` plots those same counts as stacked bars. The height of each bar gives the total for one role, and the colored segments show how that total breaks down by academic framing.

`summary_source_by_role.csv` groups those roles by source type so I can compare, for example, how often campus publications and counseling resources discuss gaming as a problem. Each row of the dataset contributes one count to each table. A source that supplies several passages can therefore contribute more than once.

The initial dataset passed the structural checks.

## Scholarly context

- Bowker and Star’s *Sorting Things Out* (1999) treats classification as a choice with consequences. That helps me ask what disappears when I give a passage one primary label, especially when it presents gaming as both social connection and distraction. [MIT Press](https://mitpress.mit.edu/9780262024617/sorting-things-out/)
- Bender and Friedman’s “Data Statements for Natural Language Processing” (2018) argues for documenting the context and limits of datasets. I apply that principle by describing who produced these passages, which audiences they address, and how gaps in access shape the collection. [Transactions of the Association for Computational Linguistics](https://aclanthology.org/Q18-1041/)
- Schmitt and Livingston’s “Video Game Addiction and College Performance Among Males” (2015) examines gaming and college outcomes in a specific sample of male first-year students. It gives me a comparison point for asking how public sources carry a study’s population, measures, and limitations into advice about college students. [Published study](https://doi.org/10.1089/cyber.2014.0403)

## Audit plan

I will audit the Kaggle dataset *Gaming vs Academic Performance*. I will verify that that it is synthetic against the data card, record the version and license, and look for generation documentation. In Python, I will profile the columns, types, missing values, duplicates, and distributions. I will examine how the data represent gaming, academic success, and problematic use. If the documentation specifies generation rules, I will compare them with the patterns in the records. [Kaggle dataset](https://www.kaggle.com/datasets/aiexplorer77/gaming-vs-academic-performance)

The custom dataset records public passages. The Kaggle dataset appears to use student-level records. I will compare their categories and assumptions in a table. For example, I will check which measures can represent differences among playing to unwind, playing to make friends, and playing in ways a source says interfere with coursework. I will document where the datasets lack shared identifiers or measure different things and explain what those gaps reveal about their representations.

## Reflection and feedback

In Milestone 1, I planned to scrape posts from Reddit or TikTok. I ran into API access and scraping issues, so I switched to published articles and campus guidance. These sources were easier to find through search and collect by hand.

Coding individual passages helped me distinguish why people play from what a source says about schoolwork. In 28 of the 43 passages, the source leaves the academic effect unstated. I’d like feedback on whether to keep passages about social belonging when they make no academic claim, and on how to decide when two statements from one article should become separate rows.

## Files

- [items.csv](items.csv) — initial dataset
- [codebook.md](codebook.md) — fields and annotation rules
- [validate.py](validate.py) — validation script that produces the tables and chart
- [summary_role_by_framing.csv](summary_role_by_framing.csv) — passage counts by gaming role and academic framing
- [summary_source_by_role.csv](summary_source_by_role.csv) — passage counts by source type and gaming role
- [chart_role_by_framing.png](chart_role_by_framing.png) — stacked bar chart of the role-by-framing table
