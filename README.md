# Writeup

<!-- <div align="center">
  <img width="45%" alt="" src="">
  <img width="45%" alt="" src="">
  <img width="45%" alt="" src="">
  <img width="45%" alt="" src="">

  <p>Words go here.</p>
</div> -->

## 0 Choosing a dataset to explore

The data I explored was a subset of [The General Society Survey](https://gss.norc.org/About-The-GSS) focused on stances around abortion. I found the dataset from [Rdatasets](https://vincentarelbundock.github.io/Rdatasets/articles/data.html) but it was originally created at [stevedata](http://svmiller.com/stevedata/reference/gss_abortion.html#details). I explored a variety of datasets but eventually settled on this dataset because it was a large dataset with a variety of variables in a context I could still understand. Much of the data I avoided because it would involve more data cleaning than exploration (e.g. [Unicef data](https://data.unicef.org/resources/dataset/learning-and-skills/)) or from a context I didn't fully understand (e.g. [health data](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset?select=heart.csv)). I found this dataset to be both usable and comprehensible.

## 1 Data Parsing

The first step of this was to clean the data by specifying data types, renaming columns, and filling in missing values. During this step I also viewed the raw data and explored it with the (non-visual) R methods `dim`, `view`, `summary`, and `str`.
<div align="center">
  <img height="300" alt="a" src="https://user-images.githubusercontent.com/53503018/136717881-14b7d002-cada-4171-ad32-cdaab5aa4298.png">
  <img height="300" alt="b" src="https://user-images.githubusercontent.com/53503018/136717883-aa207ceb-00b2-4259-bd9d-8323d594e036.png">
  <p>R giving parsing issues and missing values.</p>
</div>

## 2 Missing Values

I started by visualizing the number of missing value for each column. When I ignored rows with missing values it removed too much data. You can see below when I remove rows with `NA` for `ab_any`, we go from `64814` values to `36794` values. This prompted me to investigate why it was there were so many missing values.

<div align="center">
  <img width="45%" alt="0a00005c.png" src="https://user-images.githubusercontent.com/53503018/136874866-9b5d89d0-5232-49ec-9cc7-f6f16eaa1c74.png">
  <img width="45%" alt="0b00000missing_na_b.png" src="https://user-images.githubusercontent.com/53503018/136874867-819e426b-bc9a-4b7c-8842-66f9d2b324b4.png">

  <p>Bar charts of missing values.</p>
</div>

## 3 Missing Questions

I suspected that some of the missing data might be due to changes in the survey questions over the years. To visualize this, I plotted the number of missing values by year for each column and colored the bars if all of the values for that year were `NA`. Based on these graphs, saw that some questions weren't asked until the 2000s. I was able to confirm this assumption with the [archive of all GSS questionnaires](https://gss.norc.org/get-documentation/questionnaires). This meant that I needed to find a way to clean the data without dropping rows with `NA` values or the data would be skewed towards the present.

<div align="center">
  <img width="45%" alt="2scd.png" src="https://user-images.githubusercontent.com/53503018/136874948-3ac63d50-4c18-4579-99be-fd7f5190efae.png">
  <img width="45%" alt="2sce.png" src="https://user-images.githubusercontent.com/53503018/136874956-4564c8f0-c9df-41a4-a0b7-478e9c4fce2e.png">
  <img width="45%" alt="2missing_rels.png" src="https://user-images.githubusercontent.com/53503018/136874947-b975888d-e8db-4ed5-b5d1-e597ee08c5be.png">
  <img width="45%" alt="3sch.png" src="https://user-images.githubusercontent.com/53503018/136875029-65aaf7bb-8dff-4ba1-aefc-29cf462a7e31.png">

  <p>Missing values by year and example questionnaire from 1990.</p>
</div>

## 4 Missing Questions Pt. 2

By chance, I was coloring this graph by different values and decided to color it by the proportion of `NA` values. I noticed while some years would have `0.37` or `0.67` missing values. It didn't make sense that that many people would choose not to answer a question, because previous years would have only `0.05` missing values. This prompted me to investigate the questionnaires themselves, and I found that at some point there started to be multiple versions of the questionnaire. Some years only 1 of 3 of the questionnaires would have questions about abortion, so we see there would be `0.37` missing values.

<div align="center">
  <img width="85%" alt="3sci.png" src="https://user-images.githubusercontent.com/53503018/136875031-9cb46e4a-b6f5-4c66-a352-e15760a68417.png">
  <img width="45%" alt="3scg.png" src="https://user-images.githubusercontent.com/53503018/136875028-98f4e0b5-48d5-4d84-a1e2-936fb53e3421.png">
  <img width="45%" alt="3scf.png" src="https://user-images.githubusercontent.com/53503018/136875026-18af4569-b990-4517-8308-896880e85ed3.png">

  <p>Proportion of missing values by year and multiple questionnaires for 2000.</p>
</div>

## 4.5 Fill Missing Values

Now that I knew the reason for the missing values, I had a better idea of how to replace them. I will skip the details for brevity, but besides `religious_activity` I was able to replace the `NA` values with something to represent that a question was not asked.

With this long step of cleaning data over, I could start plotting in Tableau.

<div align="center">
  <img width="45%" alt="0a00005c.png" src="https://user-images.githubusercontent.com/53503018/136874866-9b5d89d0-5232-49ec-9cc7-f6f16eaa1c74.png">
  <img width="45%" alt="0c00005e.png" src="https://user-images.githubusercontent.com/53503018/136874870-16b44c0a-0cf8-48a9-8419-5ae742a3ea8f.png">

  <p>Old data on left, cleaned data on right.</p>
</div>

## 5 Bars

<div align="center">
  <img width="45%" alt="Abortion Stances by Hispanic" src="https://user-images.githubusercontent.com/53503018/136875278-62288e2a-bb64-4050-b18f-8e8cda697c60.png">
  <img width="45%" alt="Abortion Stances by Party Bar" src="https://user-images.githubusercontent.com/53503018/136875282-647b6164-3f6b-4105-81cc-70a24c2c79e3.png">
  <img width="45%" alt="Abortion Stances by Party Bar 2" src="https://user-images.githubusercontent.com/53503018/136875280-eb7cfd80-e46b-450e-80b9-32ff357d3efa.png">
  <img width="45%" alt="Abortion Stances by Sex" src="https://user-images.githubusercontent.com/53503018/136875284-652698de-b7c2-4da2-8fe4-34b5c8c81e62.png">

  <p>Bar charts for abortion stances against different variables with average and 95% ci.</p>
</div>

## 6 Correlations

<div align="center">
  <img width="45%" alt="1Abortion Stances by Party.png" src="https://user-images.githubusercontent.com/53503018/136875123-f6b1b241-cb3f-4b3c-9828-d4038137fac3.png">
  <img width="45%" alt="1Abortion Stances by Religious Activity.png" src="https://user-images.githubusercontent.com/53503018/136875124-247a4bf0-752d-448c-bacd-f1a10c0b99ae.png">
  <img width="45%" alt="1Abortion Stances by Education.png" src="https://user-images.githubusercontent.com/53503018/136875120-d9332ba1-408f-40c9-bc43-37d9c1840f36.png">
  <img width="45%" alt="1Abortion Stances by Age.png" src="https://user-images.githubusercontent.com/53503018/136875117-1bbdb8b5-8beb-4a3a-b494-473410d81c59.png">

  <p>Line plots to show correlations between abortion stances and <code>Party</code>, <code>Religious Activity</code>, <code>Education</code>, and <code>Age</code>.</p>
</div>

## 7 Time

<div align="center">
  <img width="45%" alt="Abortion Stances by Year" src="https://user-images.githubusercontent.com/53503018/136875293-45133031-3bf2-413f-9bd2-db91f33d4454.png">
  <img width="45%" alt="Abortion Stances by Sex over Time" src="https://user-images.githubusercontent.com/53503018/136875290-c6ec8ef8-422f-4f96-bb98-dcf7868c79ba.png">
  <img width="45%" alt="Abortion Stances by Party over Time" src="https://user-images.githubusercontent.com/53503018/136875289-8fa623f7-eeda-4c00-9806-cc2440835648.png">

  <p>Abortion stances by year overall and for both <code>Sex</code> and <code>Party</code>.</p>
</div>

## Variable Table

| Variable | Description |
|---|---|
| id | a unique respondent identifier |
| year | the survey year |
| age | the respondent's age in years |
| race | the respondent's race, as character variable |
| sex | the respondent's gender, as character variable |
| hispaniccat | the respondent's Hispanic ethnicity, as character variable |
| educ | how many years the respondent spent in school |
| partyid | the respondent's party identification, as character variable |
| relactiv | the self-reported religious activity of the respondent on a 1:11 scale |
| abany | a binary variable that equals 1 if the respondent thinks abortion should be legal for any reason. 0 indicates no support for abortion for any reason. |
| abdefect | a numeric vector that equals 1 if the respondent thinks abortion should be legal if there is a serious defect in the fetus. 0 indicates no support for abortion in this circumstance. |
| abnomore | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a woman is pregnant but wants no more children. 0 indicates no support for abortion in this circumstance. |
| abhlth | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a pregnant woman's health is in danger. 0 indicates no support for abortion in this circumstance. |
| abpoor | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a pregnant woman is poor and cannot afford more children. 0 indicates no support for abortion in this circumstance. |
| abrape | a numeric vector that equals 1 if the respondent thinks abortion should be legal if the woman became pregnant because of a rape. 0 indicates no support for abortion in this circumstance. |
| absingle | a numeric vector that equals 1 if the respondent thinks abortion should be legal if a pregnant woman is single and does not want to marry the man who impregnated her. 0 indicates no support for abortion in this circumstance. |
| pid | `partyid` recoded so that 7 = NA |
| hispanic | a dummy variable that equals 1 if the respondent is any way Hispanic |