# Instructor Feedback for Milestone 2

I really like the personal and cultural motivation behind this project. Your discussion of night-owl schedules, academic pressure, and the normalization of sacrificing sleep gives you a strong reason to ask what numerical sleep data can and cannot show. I also appreciate that you documented the files clearly, preserved the original dataset, developed a validation script, and explained your use of AI.

The main issue is how the custom dataset and existing-data audit relate to one another. Currently, your custom dataset is a 75-row sample from the same research dataset you intend to audit. I would like to see more of your own interpretive data creation, but I think you can develop that component without abandoning the work you have already completed.

## Initial Custom Dataset

The CMU sleep data is a useful choice for your existing-data audit. For the custom dataset, I would consider collecting material that helps you investigate how sleep is understood and discussed in college life.

For example, you could build a focused collection of campus newspaper articles, university wellness pages, advice posts, or other public materials about all-nighters, productivity, stress, and academic success. You do not need to collect every kind of source. Choosing a particular setting or comparison would make the project more manageable.

Your fields might record:

- The source, date, and type of speaker or institution.
- What explanation is offered for insufficient sleep.
- Whether sleep loss is normalized, criticized, or treated as unavoidable.
- What counts as academic success.
- Who is expected to take responsibility for changing sleep habits.
- Your interpretation, supporting evidence, and any uncertainty.

This would let you compare what becomes visible in cultural discussions with what becomes measurable in the CMU research dataset. You would not need to argue that those materials explain the behavior of the particular students who participated in the study.

If this would be too substantial a change, another possibility is to create a carefully documented dataset of the CMU variables, their definitions, sources, assumptions, and limitations. That could make the construction of the research dataset your central object. However, the current participant subset alone does not yet demonstrate the item-by-item interpretive work I would like to see in the custom-data component. Happy to brainstorm further ideas!

### Sampling and Dataset Scope

I appreciate that you explain your selection of fifteen records from each of the five studies and acknowledge that this changes the proportions in the original dataset.

The studies differ in size and context, so giving each one equal weight may produce different patterns from analyzing all 634 records. A balanced sample is not inherently wrong, but it should serve a particular question. What does comparing equally sized study groups help you investigate?

Because the complete dataset is manageable, I would use all 634 records for the audit. You could retain the balanced sample as an additional comparison if you explain its purpose.

The script currently checks whether the selected records occur in the original data, but it does not recreate the selection. If you keep the sample, include the sampling operation and random seed so another reader can reproduce it.

### Derived Fields and Interpretive Decisions

Converting sleep time from minutes to hours is useful, and your coverage categories draw attention to differences in how much tracking data is available. I would make clear that the 50% and 80% thresholds are your analytical choices rather than categories supplied by the original researchers. You might also investigate whether changing those thresholds affects your findings.

Several other added fields contain the same value for every record, including:

- `academic_load_context_available`
- `reason_for_sleep_pattern_available`
- `employment_context_available`
- `audit_note`

These observations may be important, but repeating a limitation across all 75 participants does not create additional participant-level information. I would move those points into the documentation or a separate variable-audit file unless they can meaningfully differ across records.

That distinction will help clarify what belongs to an individual observation and what describes the dataset as a whole.

## Auditing the CMU Sleep Dataset

I would make the construction of the original measurements a central part of the audit. A field such as `TotalSleepTime` can look straightforward, but it represents a sequence of decisions about sensing, identifying sleep episodes, defining a main sleep period, excluding observations, and calculating averages.

Your project becomes particularly interesting when you ask how those decisions shape the relationship between the measurements and students’ lived experiences.

I would trace how the study moves from Fitbit measurements to the variables in the published dataset. Which rules distinguish the main sleep episode from daytime sleep? How are interrupted or unusual schedules represented? What happens when tracking data is incomplete?

Document those definitions using the study’s methods and explain what they make visible or obscure. This connects directly to your interest in night-owl schedules and academic pressure: two students with similar average sleep durations may have very different routines and reasons for them.

The goal does not need to be proving that the measurements are wrong. Explaining what they measure, how they were constructed, and what questions they cannot answer would already be a useful audit.

### Academic Workload and Missing Context

I would also revise the claim that academic-load context is entirely unavailable. The dataset includes `term_units` and `Zterm_units_ZofZ`, which provide measures of course load.

Those fields do not describe everything that might make a student’s workload demanding. Assignments, exams, employment, care responsibilities, and the student’s experience of their courses may still be absent.

That more precise distinction is a stronger audit finding: the dataset represents workload in a particular way while leaving other dimensions unmeasured. I would investigate how the course-unit variables were constructed, how they differ across studies, and where values are missing. You might even think about how you would add in more detailed work load data that fits closer to what you envisioned.

Your `audit_missing_original_fields` column also identifies missing values stored as spaces. This is a useful finding because those values can be missed by a standard Pandas missing-value check. Please include the cleaning code that detects them and apply it to the complete dataset.

### Demographic Categories and Data Ethics

I appreciate your caution about making causal or moral judgments about individual students. I would extend that attention to the demographic categories themselves.

Investigate how race and gender were obtained and grouped in the original study. What distinctions were preserved, which were collapsed, and what analytical purpose did those choices serve? Use the study documentation to explain those decisions rather than treating the categories as self-explanatory descriptions of students.

The participant identifiers also deserve a brief explanation. They are useful for tracing selected records back to the original dataset, but pseudonymous identifiers do not by themselves guarantee anonymity. You could explain that your analysis will not attempt to identify participants and will avoid highlighting unusually specific combinations of sensitive attributes.

## Computational Work and Reproducibility

Your validation script provides a solid foundation. It runs and checks record membership, the conversion from minutes to hours, coverage categories, and summary statistics.

However, the missing-value check does not yet handle whitespace-only entries. The script can therefore report no missing values even when your own audit fields identify them. I would address that discrepancy before treating the validation output as complete.

For the next stage, I would extend the workflow so that it:

1. Reads and preserves the original dataset.
2. Converts blank or whitespace-only entries into explicit missing values in a working copy.
3. Recreates any sample and derived fields.
4. Checks all 634 records.
5. Summarizes coverage and missingness by study.
6. Produces a small number of visualizations tied to your audit questions.

For example, you could compare how a pattern changes when using the complete dataset versus the balanced sample, or when separating records by tracking coverage.

If you investigate GPA, consider differences among institutions, study periods, prior cumulative GPA, and course-load measures. A scatterplot can help you explore a relationship, but an association between sleep and GPA would not establish that sleep caused the difference.

## Scholarship and Reflection

The PNAS article is an important scholarly source because it explains the research that produced the dataset. The CMU repository is also useful documentation, but I would add one or two scholarly sources that develop the broader cultural or methodological question.

Relevant directions include:

- College sleep culture, academic pressure, and all-nighters.
- The possibilities and limitations of wearable sleep measurements.
- The history of measuring and defining sleep.
- Ethical questions around student, health, or educational data.

Use those sources to inform your decisions. For example, scholarship might help you question a measurement definition, develop categories for your custom dataset, or distinguish individual habits from institutional expectations.

Your README already contains thoughtful reflection, especially where you recognize that similar measurements can represent different experiences. I would develop that further by explaining how working with the data changed your question. What did you initially expect the dataset to show, and what did you discover it could not establish?

Your AI disclosure is also helpful. You could make it more specific by describing a suggestion you accepted, revised, or rejected and explaining how you checked it.

## Priorities for the Final Project

For the next stage, I would prioritize:

- Defining a focused custom dataset and explaining how it connects to the CMU audit.
- Auditing the complete CMU dataset, with any smaller sample serving a clearly stated purpose.
- Investigating how sleep, workload, GPA, race, and gender were represented.
- Separating dataset-level observations from participant-level fields.
- Correcting the academic-load description and handling whitespace-based missing values.
- Making selection, cleaning, and derived fields reproducible.
- Adding scholarship and expanding the reflection on your research decisions and AI verification.

You have a thoughtful foundation, particularly in your recognition that numerical similarity does not imply identical lived experience. Developing that insight through your own interpretive data and a closer examination of the original measurements would give the project a clear cultural contribution.
