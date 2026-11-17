# Instructor Feedback for Milestone 2

This is a very strong and coherent submission, and I really like the shift from trying to measure student behavior to investigating how institutions and campus publications define productive and distracting social-media use. You now have a clear cultural question that cannot be answered through screen-time totals alone.

I’m particularly impressed by the documentation. You explain how forty web pages became 64 passages, how those passages became structured records, what paraphrasing leaves out, and why you introduced a conditional category. The computational work, audit plan, reflection, and scholarship also support the same question rather than feeling like separate assignment components.

For the next stage, I would focus on making the selection and interpretation more traceable, comparing passage-level and source-level patterns, and investigating how the existing datasets construct their measures of distraction and productivity.

## Initial Custom Dataset

Using a passage rather than an entire page as the unit of analysis makes sense because one page can contain several recommendations or competing claims. Your current collection is a strong initial basis for developing that approach. Further collection should address the coverage and comparisons you want to investigate in the final project.

The important next step is explaining how the composition of the collection shapes the patterns you can identify.

### Passage Selection and Source Coverage

Some pages contribute more passages than others: 22 pages contribute one passage, twelve contribute two, and six contribute three. That means certain pages receive more weight in the overall counts.

I would keep the passage-level analysis but add a source-level comparison. For example, does the same pattern appear when each page contributes only one count for each framing it contains? If the results differ, that could be interesting: some sources may repeat or elaborate a particular framing more extensively.

The collection also combines different source types. Campus publications contribute 31 passages, while counseling and wellness pages, platform announcements, and news coverage contribute only two passages each. That is not inherently a problem, but comparisons involving those smaller groups will be limited. You could make the emphasis on campus publications part of the scope or distinguish those sources from other kinds of advice.

To make the selection process clearer, I would document:

- The search engine or platform used.
- The exact queries in each search cluster.
- When you searched and how far into the results you looked.
- How you selected pages and passages.
- What you excluded.
- Why you stopped collecting when you did.

You could retain the mixed source base or narrow it to a more defined comparison. Either approach could work, as long as the selection logic and claims remain aligned.

### Interpretive Categories and Uncertainty

The distinction among `distracting`, `productive`, and `conditional` works well, and I especially like that `boundary_rule` preserves some of the qualifications those labels would otherwise flatten. The purpose, evidence, and responsibility fields also give you several ways to investigate how this advice works.

I would add a few examples showing how you assigned the categories to your final data essay. Difficult cases would be particularly useful. For example:

- What makes a passage primarily about `study_focus` rather than `procrastination` or `wellbeing`?
- How do you distinguish `staff_expertise` from `interviewee_opinion`?
- When is responsibility `individual`, `shared`, or `institutional`?
- What do you do when a passage supports more than one interpretation?

You do not need to eliminate ambiguity. You could record alternative labels or uncertainty in `interpretation_note`, or add a separate field if that would be easier to analyze. I’m more interested in seeing how you worked through a difficult decision than in having every record appear equally certain.

### Source Evidence and Speaker Context

Paraphrasing and linking to the source is a thoughtful starting point. However, paraphrase alone can make it difficult for someone else to evaluate your classification because they are reading your representation of the passage rather than the language you interpreted.

I would preserve a short source excerpt where it is needed to support the coding, with clear attribution and a source link. You could keep that evidence in your research files while using paraphrases primarily in the public essay.

Speaker roles also matter. Is the passage a student’s account, a staff recommendation, a journalist’s interpretation, or an institutional statement? Removing someone’s name may be appropriate, but removing their role could erase an important distinction between lived experience and institutional advice.

Also, paraphrasing does not necessarily make a statement anonymous when you retain a searchable source URL. Think about what information is necessary for interpretation and how you will present student voices responsibly. Where permitted, an archived link or preserved research copy could help you revisit evidence if a page changes.

## Computational Work and Interpretation

Your script runs successfully and performs useful checks on required fields, controlled categories, duplicates, and passage formatting. It also regenerates the summary table and chart. That gives you a strong foundation for extending the analysis.

The initial pattern is interesting: study-focus passages tend to frame social media as distracting or conditional, while professional-networking and community-belonging passages are more often productive. The responsibility fields offer another useful direction. Who is expected to regulate behavior, and when does advice point students toward institutional services or approved forms of participation?

I would continue distinguishing those findings from claims about what social media objectively does. Your dataset shows how selected sources define appropriate use, and those patterns are partly shaped by your searches and coding choices. That is already a meaningful cultural finding.

For the final project, I would consider:

- A source-level version of the framing chart.
- A comparison of responsibility across distracting, productive, and conditional framings.
- A table showing what kinds of evidence support each framing.
- A few close readings that explain the patterns and their exceptions.

You do not need to produce every possible visualization. Choose the ones that help develop an argument, and use individual passages to show what the counts cannot explain on their own.

## Auditing the Kaggle and Mendeley Datasets

Comparing definitions rather than trying to match individual students is a strong connection between the two parts of your project. Your custom dataset examines how campus sources define distraction; the audit can investigate how a tabular dataset turns distraction and productivity into variables and scores.

I also appreciate your correction that the Mendeley dataset identifies the Kaggle dataset as one of its inputs. They should therefore be treated as connected sources rather than independent evidence.

I would add direct dataset citations, including creator names, versions, access dates, licenses, and the specific files you examined.

For the Kaggle data, investigate whether the records represent observed participants, simulated cases, or some other process. What documentation is available about recruitment, location, dates, measurement, and consent? How were `focus_score` and `productivity_score` constructed?

Unusually clean values, regular distributions, or strong correlations can motivate questions, but they do not establish that the data is synthetic. Distinguish what you can verify from what remains undocumented.

The Mendeley description of joining educational sources through “unique identifiers” also deserves attention. An identifier can be unique within one dataset without referring to the same person in another. I would look for documentation explaining what was matched, how the match was established, and whether the resulting rows have a defensible relationship.

### Comparing Definitions of Distraction

Your proposed checklist is a useful way to connect the audit to the custom dataset. The passages distinguish purpose, timing, notifications, intention, platform, content, and other contextual features. Which of those distinctions can the tabular data represent?

I would also ask what the audited dataset contains that your corpus does not. The comparison will be stronger if you examine the possibilities and limits of both approaches rather than assuming one is inherently better.

Questions worth pursuing include:

- Who defines productivity in each source?
- Is distraction treated as a behavior, a measurement, or a judgment?
- Can the same activity be productive in one context and distracting in another?
- Which differences disappear when an experience becomes a single score?
- What assumptions would carry forward if someone used the dataset to predict student outcomes or recommend an intervention?

These questions could help you move from listing missing fields to explaining how different representations support different claims.

## Scholarship and Reflection

Your three scholarly sources are relevant and clearly connected to the project. As the audit develops, an additional source on educational-data provenance, synthetic data, or the measurement of student productivity could deepen the comparison. I would add one if it helps resolve a specific question, rather than expanding the bibliography for its own sake.

Your reflection also responds well to earlier feedback and explains what is working, what remains uncertain, and what might change. For the final version in your data essay, you could develop an example of a category or interpretation that changed during collection and explain what prompted that revision.

Please also include an AI-use statement. If AI assisted, explain what it contributed and how you checked or revised the output. If you did not use AI, a brief statement would clarify that.

## Priorities for the Final Project

For the next stage, I would prioritize:

- Documenting the search and passage-selection process.
- Preserving enough source language and speaker context to support your interpretations.
- Adding worked coding examples and documenting uncertainty.
- Comparing passage-level findings with source-level summaries.
- Investigating the provenance and construction of the Kaggle measures.
- Tracing the relationship between the Kaggle and Mendeley datasets.
- Adding complete dataset citations and an AI-use statement.

You have already established a thoughtful project with a clear cultural contribution. The next step is to use the relationship between close reading, computational summaries, and the audit to explain what changes when “digital distraction” becomes something that can be categorized and counted.
