# Writeup

<!-- <div align="center">
  <img width="45%" alt="" src="">
  <img width="45%" alt="" src="">
  <img width="45%" alt="" src="">
  <img width="45%" alt="" src="">

  <p>Words go here.</p>
</div> -->

## Choosing a dataset to explore

The data I explored was a subset of The General Society Survey [^1] focused on stances around abortion. I found the dataset from Rdatasets [^2] but it was originally created at stevedata [^3]. I explored a variety of datasets but eventually settled on this dataset because it was a large dataset with a variety of variables in a context I could still understand. Much of the data I avoided because it would involve more data cleaning than exploration (e.g. Unicef data [^4]) or from a context I didn't fully understand (e.g. health data [^5]). I found this dataset to be both usable and comprehensible. For brevity, I have described each variable in a table at the bottom of this document.

### Initial Question

Given this survey data, what different demographics tend to be in favor of or against abortion?

## Why am I having parsing errors?

The first step was to clean the data by specifying data types, renaming columns, and filling in missing values. During this step I also viewed the raw data and explored it with the (non-visual) R methods `dim`, `view`, `summary`, and `str`. This step is simple but it was an important step in the data exploration because all the parsing errors forced me to become familar with the format of the data.
<div align="center">
  <img height="300" alt="a" src="https://user-images.githubusercontent.com/53503018/136717881-14b7d002-cada-4171-ad32-cdaab5aa4298.png">
  <img height="300" alt="b" src="https://user-images.githubusercontent.com/53503018/136717883-aa207ceb-00b2-4259-bd9d-8323d594e036.png">
  <p>R giving parsing issues and missing values.</p>
</div>

## How many missing values are there?

I started by visualizing the number of missing value for each column. When I ignored rows with missing values it removed too much data. You can see below when I remove rows with `NA` for `ab_any`, we go from `64814` values to `36794` values. This prompted me to investigate why it was there were so many missing values.

<div align="center">
  <img width="45%" alt="0a00005c.png" src="https://user-images.githubusercontent.com/53503018/136874866-9b5d89d0-5232-49ec-9cc7-f6f16eaa1c74.png">
  <img width="45%" alt="0b00000missing_na_b.png" src="https://user-images.githubusercontent.com/53503018/136874867-819e426b-bc9a-4b7c-8842-66f9d2b324b4.png">

  <p>Bar charts of missing values.</p>
</div>

## Why are there so many missing values?

Suspecting the missing data was because of changes in the survey questions I plotted the number of missing values by year and colored the bars if all of the values for that year were `NA`. Based on these graphs, I saw that some questions weren't asked until the 2000s. I was able to confirm this assumption with the archive of all GSS questionnaires [^6]. This meant that I needed to find a way to clean the data without dropping rows with `NA` values or the data would be skewed towards the present.

<div align="center">
  <img width="45%" alt="2scd.png" src="https://user-images.githubusercontent.com/53503018/136874948-3ac63d50-4c18-4579-99be-fd7f5190efae.png">
  <img width="45%" alt="2sce.png" src="https://user-images.githubusercontent.com/53503018/136874956-4564c8f0-c9df-41a4-a0b7-478e9c4fce2e.png">
  <img width="45%" alt="2missing_rels.png" src="https://user-images.githubusercontent.com/53503018/136874947-b975888d-e8db-4ed5-b5d1-e597ee08c5be.png">
  <img width="45%" alt="3sch.png" src="https://user-images.githubusercontent.com/53503018/136875029-65aaf7bb-8dff-4ba1-aefc-29cf462a7e31.png">

  <p>Missing values by year and example questionnaire from 1990.</p>
</div>

## Why are there so many missing values? Pt. 2

I was decided to color by the proportion of `NA` values and noticed while some years would have `0.37` or `0.67` missing values. This prompted me to investigate the questionnaires themselves [^6], and I found that the GSS had started to give multiple versions of the questionnaire. Some years only 1 of 3 of the questionnaires would have questions about abortion, so there would be `1/3 = 0.37` missing values.

<div align="center">
  <img width="85%" alt="3sci.png" src="https://user-images.githubusercontent.com/53503018/136875031-9cb46e4a-b6f5-4c66-a352-e15760a68417.png">
  <img width="45%" alt="3scg.png" src="https://user-images.githubusercontent.com/53503018/136875028-98f4e0b5-48d5-4d84-a1e2-936fb53e3421.png">
  <img width="45%" alt="3scf.png" src="https://user-images.githubusercontent.com/53503018/136875026-18af4569-b990-4517-8308-896880e85ed3.png">

  <p>Proportion of missing values by year and multiple questionnaires for 2000.</p>
</div>

## How can I fix these missing values?

Now that I knew the reason for the missing values, I had a better idea of how to replace them without misrepresenting the data. I will skip the details for brevity, but besides `religious_activity` I was able to replace the `NA` values with something to represent that a question was not asked.

<div align="center">
  <img width="45%" alt="0a00005c.png" src="https://user-images.githubusercontent.com/53503018/136874866-9b5d89d0-5232-49ec-9cc7-f6f16eaa1c74.png">
  <img width="45%" alt="0c00005e.png" src="https://user-images.githubusercontent.com/53503018/136874870-16b44c0a-0cf8-48a9-8419-5ae742a3ea8f.png">

  <p>Old data on left, cleaned data on right.</p>
</div>

With this long step of cleaning data over, I could start plotting in Tableau.

## Are there any obvious differences between demographics?

I started by creating bar charts of some nominal variables (`Hispanic`, `Party`, `Sex`) against Abortion stances. I had expected to see more difference in these stances between groups, especially between the sexes, but it didn't seem there was a significant difference. One unexpected thing this did highlight was differences between the different reasons for abortion. Some reasons like health were more accepted than a reason like poverty accross these demographics.

<div align="center">
  <img width="45%" alt="Abortion Stances by Hispanic" src="https://user-images.githubusercontent.com/53503018/136875278-62288e2a-bb64-4050-b18f-8e8cda697c60.png">
  <img width="45%" alt="Abortion Stances by Party Bar" src="https://user-images.githubusercontent.com/53503018/136875282-647b6164-3f6b-4105-81cc-70a24c2c79e3.png">
  <img width="45%" alt="Abortion Stances by Party Bar 2" src="https://user-images.githubusercontent.com/53503018/136875280-eb7cfd80-e46b-450e-80b9-32ff357d3efa.png">
  <img width="45%" alt="Abortion Stances by Sex" src="https://user-images.githubusercontent.com/53503018/136875284-652698de-b7c2-4da2-8fe4-34b5c8c81e62.png">

  <p>Bar charts for abortion stances against different variables with average and 95% ci.</p>
</div>

## Are there any correlations?

For variables that I thought could be treated as ordinal, like `Religious Activity`, `Age`, `Education`, or `Party` (adjusted to a numerical scale from Democratic to Republican). By plotting on a simple line chart I was able to see some simple linear correlations for `Education`, `Age`, and `Party`. `Religious Activity` (on scale from 1:11) had some interesting behaviour once it got to `11` but I was unable to find the original scale from the questionnaires to find out what this meant because the questionnaire had become computerized which made it much harder to search for a specific question.

<div align="center">
  <img width="45%" alt="1Abortion Stances by Party.png" src="https://user-images.githubusercontent.com/53503018/136875123-f6b1b241-cb3f-4b3c-9828-d4038137fac3.png">
  <img width="45%" alt="1Abortion Stances by Religious Activity.png" src="https://user-images.githubusercontent.com/53503018/136875124-247a4bf0-752d-448c-bacd-f1a10c0b99ae.png">
  <img width="45%" alt="1Abortion Stances by Education.png" src="https://user-images.githubusercontent.com/53503018/136875120-d9332ba1-408f-40c9-bc43-37d9c1840f36.png">
  <img width="45%" alt="1Abortion Stances by Age.png" src="https://user-images.githubusercontent.com/53503018/136875117-1bbdb8b5-8beb-4a3a-b494-473410d81c59.png">

  <p>Line plots to show correlations between abortion stances and <code>Party</code>, <code>Religious Activity</code>, <code>Education</code>, and <code>Age</code>.</p>
</div>

## What effect has time had on abortion stances?

I plotted against time next because of the correaltion with `Age` shown above and I just suspected there would be a pattern. I was surprised that overall there wasn't much change in the proportion of answers to questions on abortion. I did however notice the distinction between reasons for abortion even more clearly than in the bar charts. The chart by party over time was most interesting because you can see the stances on abortion diverge among party lines with the most Democratic `party` encoded as `-3` and the most Republican encoded as `3`.

<div align="center">
  <img width="45%" alt="Abortion Stances by Year" src="https://user-images.githubusercontent.com/53503018/136875293-45133031-3bf2-413f-9bd2-db91f33d4454.png">
  <img width="45%" alt="Abortion Stances by Sex over Time" src="https://user-images.githubusercontent.com/53503018/136875290-c6ec8ef8-422f-4f96-bb98-dcf7868c79ba.png">
  <img width="45%" alt="Abortion Stances by Party over Time" src="https://user-images.githubusercontent.com/53503018/137047552-7b6a2da4-a841-4be6-839e-83e7a2625aed.png">

  <p>Abortion stances by year overall and for both <code>Sex</code> and <code>Party</code>.</p>
</div>

## What insights do I find most interesting?

Based on previous visualizations, I found these insights the most interesting:

1. The correlation between `Education` and abortion stances
2. The correlation between `Age` and abortion stances
3. The divergence of abortion stances by `Party` over time
4. The difference between reasons for abortion
5. The reason for missing values (survey question changes)

I created new visuals to highlight each of these visuals besides the last point (because it was part of data cleaning). I combined points 2 and 4 by grouping by reason before age.

<div align="center">
  <img width="85%" alt="Abortion Stances by Age" src="https://user-images.githubusercontent.com/53503018/137049941-a3a961a1-f3f2-41cf-822f-a039964a1e4a.png">
  <img width="85%" alt="Abortion Stances by Education" src="https://user-images.githubusercontent.com/53503018/137049944-146be31e-8b69-4c2d-9fa7-45b80662b1d6.png">

  <p>Newly created visuals.</p>
</div>

## Summary of Lessons Learned

Now let us return to the original question:

> Given this survey data, what different demographics tend to be in favor of or against abortion?

I learned a lot during the data exploration. A lot fo the interesting moments and stuff was about data parsing. Then it was intersting correlations. I found it really satisfying how the line graph was able to visualize how stances on abortion diverged along party lines. I also found it surprising I wasn't able to find significant differences among certain demographics like sex where I expected there to be a major difference. This is the final visualization I made that emphasizes the points that I think were the most interesting as described in the previous section.

<div align="center">
  <img width="85%" alt="FinalVisual" src="https://user-images.githubusercontent.com/53503018/137048935-67102380-3c5c-4033-8ad3-c96cde57f4d1.png">

  <p>Final visualization emphasizing <code>Age</code>, <code>Education</code>, and <code>Party</code> (over time)</p>
</div>

## Appendix

[source code](https://github.com/Avery2/Abortion-Data-Exploration)

### Variable Description Table

| Variable | Description |
|---|---|
| id | a unique respondent identifier |
| year | the survey year |
| age | the respondent's age in years |
| race | the respondent's race, as character variable |
| sex | the respondent's gender, as character variable |
| education | how many years the respondent spent in school |
| party | the respondent's party identification, as character variable |
| religious_activity| the self-reported religious activity of the respondent on a 1:11 scale |
| ab_any | a binary variable that equals 1 if the respondent thinks abortion should be legal for any reason. 0 indicates no support for abortion for any reason. |
| ab_defect | a numeric vector that equals 1 if the respondent thinks abortion should be legal if there is a serious defect in the fetus. 0 indicates no support for abortion in this circumstance. |
| ab_nomore | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a woman is pregnant but wants no more children. 0 indicates no support for abortion in this circumstance. |
| ab_hlth | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a pregnant woman's health is in danger. 0 indicates no support for abortion in this circumstance. |
| ab_poor | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a pregnant woman is poor and cannot afford more children. 0 indicates no support for abortion in this circumstance. |
| ab_rape | a numeric vector that equals 1 if the respondent thinks abortion should be legal if the woman became pregnant because of a rape. 0 indicates no support for abortion in this circumstance. |
| ab_single | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a pregnant woman is single and does not want to marry the man who impregnated her. 0 indicates no support for abortion in this circumstance. |
| hispanic | a dummy variable that equals 1 if the respondent is any way Hispanic |

[^1]: https://gss.norc.org/About-The-GSS
[^2]: https://vincentarelbundock.github.io/Rdatasets/articles/data.html
[^3]: http://svmiller.com/stevedata/reference/gss_abortion.html#details
[^4]: https://data.unicef.org/resources/dataset/learning-and-skills/
[^5]: https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset?select=heart.csv
[^6]: https://gss.norc.org/get-documentation/questionnaires
