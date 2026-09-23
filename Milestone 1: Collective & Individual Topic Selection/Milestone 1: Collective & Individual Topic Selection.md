# Milestone 1: Collective & Individual Topic Selection

## Group Theme

**What is your shared area of interest? What kinds of cultural objects, practices, or phenomena fall within this theme? What’s included and what’s beyond scope?**

- Our group's shared interest is how academic performance depends on different factors, including gaming, social media, mental health, and sleep.
- For academic performance, we can include GPA, test scores, transcripts, hours of studying, etc. in our scope. Only university-level academic performance is considered.
- Differences in educational programs and teaching quality is beyond our scope. Countries other than the US would also be out of our scope.

## Individual Ideas

**What dataset is each group member considering creating vs. auditing? You should detail both as much as you can here. You can post links or screenshots. You should also detail how your idea connects to the group theme. The core question for your dataset creation is: what cultural complexity are you trying to preserve or make visible? The core question for your dataset auditing is: how has cultural complexity been captured or erased in the dataset?**

### Tergel: How gaming affects academic performance

**Dataset creation:** I was thinking about webscraping publicly posted TikTok or Reddit content where students talk about gaming and academics in the same post. For example, videos with tags like #study and #gaming or posts in subreddits like r/GetStudying or game-specific subreddits where students mention balancing coursework and gaming. I would annotate each post/video for: platform, stated purpose of the gaming mention, genre/game mentioned, and whether the tone frames gaming as harmful, neutral, or beneficial to their academics. The complexity I want to preserve is that students themselves narrate this relationship in different ways, rather than simplifying it into a variable like number of hours played.

**Connection to group theme:** This connects to our group theme because it looks at how students themselves frame the relationship between gaming and academia, instead of just assuming a certain relationship based on quantitative variables.

**Dataset auditing:**

- [Gaming vs Academic Performance - Kaggle](https://www.kaggle.com/datasets/aiexplorer77/gaming-vs-academic-performance)
- I picked this dataset because its description openly states its own design logic. The description states that gaming was modeled so that moderate use "slightly improves cognitive performance" while excessive use "negatively impacts grades", with random noise added for variability. This meant that the dataset is fully synthetic and this isn't real data.
- **Cultural complexity erased:** Since it's generated and not collected, there's no real social context or motivation behind any row. Gaming culture is pretty much nonexistent.

### Cici: How social media affects academic performance

**Dataset creation:** A one-week social media use diary with UIUC undergraduates (target n = 20). Participants log each session with platform, purpose (coursework, family, friendship, entertainment, professional), a short open-text note, and a self-described account of their academic load that week.

This fits our group's theme because it isolates social media specifically instead of lumping it in with general lifestyle habits, and it stays inside our US university scope since I'm collecting the data myself. The complexity I want to preserve is that identical usage numbers can represent completely different things depending on the student's situation. Coordinating a group project, calling family across time zones, and scrolling for fun could all log as the same three hours, and that difference disappears completely in datasets that only track hours per day.

**Dataset auditing:** [Student Productivity & Digital Distraction Dataset - Kaggle](https://www.kaggle.com/datasets/sehaj1104/student-productivity-and-digital-distraction-dataset)

This fits our theme because it's one of the only datasets in our topic area that treats digital distraction as its own factor instead of folding it into general lifestyle data, which makes a good contrast with the diary I'm proposing.

I picked this dataset because the creator actually documented how it was built, which makes it easier to audit than most Kaggle uploads. It has around 20,000 rows, but those rows aren't 20,000 students. From what I found, it was built by merging three separate datasets (student productivity, exam prediction, and student performance) through a multi-stage pipeline, joining them on shared IDs instead of collecting one group of students. If that's right, a single row could have a student's habits from one dataset and their grades from a completely different one, matched up because the IDs lined up, not because they were ever the same person.

**Cultural complexity erased:** These datasets don't take into account the platform or purpose behind social media use (a class check-in, a call home, and scrolling for fun all count as the same hours), the country or grading system a student belongs to (there's no field for it, so the data acts like it's universal even though we scoped this to US universities), how missing values and outliers were handled before the data was published (imputing and removing them means students who didn't fit the pattern got smoothed over or dropped), and who decided the grade cutoff for the pass/fail flag, since that's never explained.

### Shreya: How student mental health affects academic performance

**Dataset creation:** We want to create a dataset that compares university students' mental health, such as stress and anxiety with academic performance measurements such as GPA, hours studied, attendance, and overall performance in courses.

**Dataset auditing:** [University Students Mental Health Dataset - Kaggle](https://www.kaggle.com/datasets/junnn0126/university-students-mental-health)

I chose this dataset because it has a lot of information about university student's mental health and other factors which would be very intuitive to understanding how mental health affects different key academic variables.

**Additional sources:**

- https://pubmed.ncbi.nlm.nih.gov/34242525/
- https://pubmed.ncbi.nlm.nih.gov/42309827/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8248896/
- https://pubmed.ncbi.nlm.nih.gov/16278502/
- https://pubmed.ncbi.nlm.nih.gov/38969021/

**Cultural complexity:** Cultural complexity can play a factor into how different cultural expectations weigh on students mental health in intersection with academic success.

### Allison: How does sleep affect academic performance?

**Dataset Creation:** Create a short sleep diary with university students that tracks sleep alongside academic behaviors for 1-2 weeks.

- Participants would record their bedtime, wake-up time, estimated hours of sleep, reason for staying up late, academic workload, and how rested/productive they felt the next day.
- Rather than only measuring hours of sleep, I want to preserve the reason behind different sleep patterns.
- This would help explore the cultural expectation that sacrificing sleep is a normal or necessary part of being a productive and successful college student.

**Scholarly Context:** [Nightly sleep duration predicts grade point average in the first year of college](https://www.pnas.org/doi/10.1073/pnas.2209123120)

- Examines the relationship between nightly sleep duration and GPA among first-year college students.
- Provides scholarly context for why sleep is relevant to academic performance and provides background for the type of sleep data I am interested in examining.

**Dataset Auditing:**

- [Nightly sleep time and GPA in first-years](https://www.stat.cmu.edu/capstoneresearch/spring2024/315files_s24/team15.html#32_Violin_Plots_of_Cumulative_GPA_Distributions_for_Students_Within_Various_Bedtime_Segments)
  - This analysis uses sleep and academic data from 634 first-year students at CMU, UWash, and Notre Dame.
  - Students' sleep was tracked using Fitbit devices, while academic performance was measured using university GPA records.
  - The data includes variables related to total sleep time, bedtime and sleep patterns, GPA, and student demographics.
  - I would audit how quantitative sleep measurements represent the relationship between sleep and academic performance and what context is lost when students' sleep habits are reduced to numerical measurements.

- [Student Insomnia and Educational Outcomes Dataset](https://data.mendeley.com/datasets/5mvrx4v62z/1)
  - I am considering this as another potential dataset for auditing because it contains data related to student sleep and academic performance.
  - I would compare what variables it includes with the first dataset and examine whether it provides additional context about students' sleep behaviors.

**Cultural complexity that may be erased:**

- These data sets can show how long and when students sleep, but quantitative measurements may not explain why a student has a particular sleep pattern.
- Staying up late to study, working a job, socializing, experiencing stress, or using social media may result in similar sleep measurements even though they represent very different student experiences.
- The data may also leave out cultural expectations surrounding productivity, such as the normalization of all-nighters or sacrificing sleep to appear hardworking.

**Connection to group theme:** This connects to our group theme because it questions not only whether sleep is associated with GPA, but also how college culture and expectations surrounding academic success may shape students' sleep habits.

## Scholarly Context

**What published scholarship helps explain your topic, sources, categories, methods, or ethical concerns?**

### Academic Performance

- https://link.springer.com/article/10.1186/s43067-024-00166-w
  - This study examines how multiple factors, including study habits, previous academic performance, extracurricular activities, and sleep relate to students' academic performance.
  - Provides scholarly context for our project by showing that academic performance is influenced by a combination of factors.

- https://psycnet.apa.org/record/2012-04281-001
  - This research reviews studies examining factors associated with university students' GPA. It considers demographic factors, prior academic performance, personality, motivation, self-regulated learning, approaches to learning, and psychosocial influences.

### Gaming, Internet Use, and Mental Health

- https://onlinelibrary.wiley.com/doi/full/10.1002/da.23094
  - Using data from 43,003 undergraduates participating in the 2017 American College Health Association-National College Health Assessment, this research examines problematic internet use/computer gaming and its relationship with mental health symptoms and academic performance.

### GPA and Grading Practices

- https://bera-journals.onlinelibrary.wiley.com/doi/10.1002/berj.4172
- https://www.tandfonline.com/doi/abs/10.1080/03075079.2025.2470297
  - These two articles expand on how the grading system came to be in the US and how grading patterns changed specifically during the pandemic.
  - They explore how GPA is not a completely fixed or consistent measure of academic performance, and that grading practices have changed historically and across institutions.

### Professor-Suggested Source

- https://direct.mit.edu/daed/article/154/3/72/131990
  - Suggested by Professor Zoe.

## Collaboration Plan

**How will your group communicate and share progress? What’s your GitHub organization strategy? How will you build the final group website and organize content?**

- Our group has created a text message group chat, and we will share our progress there.
- Each milestone will have its own folder on GitHub. The group work will have its own folder and each person will have their individual folder to add their own work to as well.
