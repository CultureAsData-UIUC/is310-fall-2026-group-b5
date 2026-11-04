# Sleep and Academic Performance: Initial Dataset Audit

## 1. Project Overview

For my individual project, I wanted to explore how sleep habits relate to academic performance among college students. This connects to our group's overall topic of how different factors, including gaming, social media, mental health, and sleep, can affect academic success.

I chose this topic because my own sleeping habits aren't very consistent, and I've always been more of a night owl. Sometimes I stay up late to finish assignments, while other times I just naturally feel more productive at night. This made me curious about whether students with different sleep schedules experience differences in their academic performance.

I'm also interested in how college culture sometimes makes staying up late seem normal, especially when students have exams, assignments, or other responsibilities. I wanted to look beyond just how many hours someone sleeps and think about why their sleeping habits might look a certain way.

For this project, I decided to audit an existing dataset rather than collect my own data. My main question is: **How do sleep duration and sleep habits relate to academic performance, and what information might be missing when we only look at numerical data?**

## 2. Dataset Source

I chose the *Nightly Sleep Time and GPA in First-Year College Students* dataset from Carnegie Mellon University's Statistics & Data Science Repository.

**Dataset:** https://cmustatistics.github.io/data-repository/psychology/cmu-sleep.html

**Related research:** https://www.pnas.org/doi/10.1073/pnas.2209123120

The original dataset contains 634 records from research involving first-year college students at three universities in the United States. It includes sleep measurements collected using Fitbit devices, along with students' GPA information.

I chose this dataset because it directly relates to my research question and fits our group's focus on U.S. university students. I also liked that it includes actual sleep measurements rather than only asking students to estimate how much they sleep.

## 3. Dataset Selection and Methodology

For my initial dataset, I selected 75 records from the original dataset.

There are five study groups represented in the data, so I randomly selected 15 records from each group to make sure they were all included. The Python script included in this folder checks that my selected records match the original dataset and verifies my calculations and audit categories. However, it does not recreate the original random sampling process. This means my sample is balanced across the study groups, although it doesn't necessarily represent the same proportions as the full dataset.

I kept all 15 original columns and added seven new columns to help with my audit. My final dataset contains 75 records and 22 columns.

Some of the original information includes:

- Student and study identifiers
- Average sleep duration
- Bedtime consistency
- Daytime sleep
- How many nights had recorded sleep data
- Cumulative GPA and term GPA

I wanted to keep the original information while adding columns that would make the data easier to understand and show where important context might be missing.

## 4. Auditing the Dataset

For my audit, I added seven columns:

| Column | What I Added |
|---|---|
| `sleep_hours_derived` | Converted sleep duration from minutes into hours |
| `sleep_data_coverage_audit` | Categorized how much sleep-tracking data was available |
| `academic_load_context_available` | Identified whether detailed academic workload information was available |
| `reason_for_sleep_pattern_available` | Identified whether the dataset explained students' sleep habits |
| `employment_context_available` | Identified whether students' employment situations were documented |
| `audit_missing_original_fields` | Recorded any missing values from the original data |
| `audit_note` | Added notes about limitations when interpreting the data |

I also separated sleep-data coverage into three categories:

- High: 80% or more of nights recorded
- Moderate: 50% to less than 80% of nights recorded
- Low: Less than 50% of nights recorded

These are categories I created for my audit, not categories from the original research.

## 5. Initial Observations

After auditing my 75 records, I found that:

- 59 records had high sleep-data coverage.
- 12 records had moderate sleep-data coverage.
- 4 records had low sleep-data coverage.

The average nightly sleep duration in my sample was approximately 6.43 hours.

One thing I noticed is that the dataset provides a lot of numerical information about students' sleep, but it doesn't really explain their sleeping habits.

For example, two students could both get six hours of sleep, but one might have stayed up studying while the other naturally prefers going to bed later. Their sleep duration would look the same in the dataset even though their experiences are different.

I think this is especially interesting because I know my own sleep schedule can change depending on my workload, but also because I tend to be more productive at night.

## 6. Cultural Context and Limitations

One of the biggest limitations I noticed is that the dataset doesn't explain why students have certain sleep schedules.

It doesn't tell us whether students stayed up late because of assignments, work, social activities, or personal preferences. I think these differences matter because they can help explain how students balance school with other parts of their lives.

I'm also interested in how college culture sometimes encourages students to sacrifice sleep to finish their work. Pulling all-nighters or staying up until early morning can feel like a normal part of college, but the dataset doesn't capture those expectations.

Another limitation is that the dataset focuses on first-year college students, so their experiences might not reflect those of students in later years.

Overall, I think the dataset is useful for identifying patterns between sleep and academic performance, but it doesn't tell the full story behind those patterns. Just because two students have similar sleep measurements doesn't mean they have similar routines or experiences.

## 7. Ethical Considerations

Since this dataset includes information about students' sleep and academic performance, I wanted to be careful about how I interpreted it.

I kept the original participant identifiers and didn't try to identify individual students. I also avoided making assumptions about why someone slept a certain amount or received a certain GPA.

For example, I wouldn't assume that a student with less sleep was irresponsible or that their sleeping habits directly caused their academic performance.

I think it's important to recognize that numerical data doesn't always explain someone's personal circumstances.

## 8. Next Steps

For the next stage of my project, I want to explore the relationship between sleep habits and academic performance more closely.

**1. Expand my dataset**

I plan to audit more records from the original dataset and see whether the patterns I noticed in my initial sample are consistent across the larger dataset.

**2. Analyze sleep duration and GPA**

I want to use Python to look at whether students who sleep different amounts tend to have different GPAs. I could also create scatterplots to visualize the relationship.

**3. Look at sleep consistency**

Since my own sleep schedule isn't very consistent, I'm particularly interested in whether having a regular bedtime matters in addition to the total amount of sleep someone gets.

I want to explore the bedtime variability measurements in the dataset and compare them with students' GPAs.

**4. Explore missing cultural context**

I also want to look into how students' workloads, personal preferences, and college culture influence their sleep habits. This could involve reviewing research about night owls, academic stress, and the expectation that students should stay up late to be productive.

**5. Connect my findings to our group project**

Eventually, I want to compare my findings with my group members' projects on gaming, social media, and mental health.

These topics overlap in a lot of ways, and I think comparing them could help us better understand the different factors that shape students' academic experiences.

## 9. AI Assistance

I used ChatGPT to help me examine the original dataset, select a sample of 75 records, add audit columns, and organize my documentation.

I also used it to help understand how the dataset's measurements could be interpreted and what information might be missing.

## 10. Files

- `cmu_sleep_audit_75.csv`: My initial audited dataset with 75 records
- `cmu-sleep.csv`: The original dataset used for my audit
- `audit_script.py`: Python script that checks the selected records, calculations, and audit categories
- `README.md`: Documentation explaining my dataset, audit process, observations, and next steps

## 11. References

Carnegie Mellon University Statistics & Data Science Repository. *Nightly Sleep Time and GPA in First-Year College Students.* https://cmustatistics.github.io/data-repository/psychology/cmu-sleep.html

*Nightly sleep duration predicts grade point average in the first year of college.* (2023). *Proceedings of the National Academy of Sciences.* https://www.pnas.org/doi/10.1073/pnas.2209123120