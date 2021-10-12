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

The first step of this was to clean the data by specifying data types, renaming columns, and filling in missing values. Here, I did the first data exploration by checking each column to get the proportion of missing values. As you can see, two columns have `p > 0.6` where `p` is the proportion of `NA` values.

<div align="center">
  <img height="300" alt="a" src="https://user-images.githubusercontent.com/53503018/136717881-14b7d002-cada-4171-ad32-cdaab5aa4298.png">
  <img height="300" alt="b" src="https://user-images.githubusercontent.com/53503018/136717883-aa207ceb-00b2-4259-bd9d-8323d594e036.png">
  <p>R giving parsing issues and missing values.</p>
</div>

## 2 R

Now that the data is at least loaded into R (ignoring the issue of so many missing values) I was able to start data exploration.

<div align="center">
  <img height="300" alt="rsca.png" src="https://user-images.githubusercontent.com/53503018/136874793-18c1902e-0790-4d27-8029-275178a516c6.png">
  <img height="300" alt="rscb.png" src="https://user-images.githubusercontent.com/53503018/136874796-81a391ea-88e7-4677-8c5a-64ce9ba4a664.png">
  <img height="300" alt="rscc.png" src="https://user-images.githubusercontent.com/53503018/136874798-cf854caf-0e2f-4b3b-82f2-89ab026ebf0b.png">

  <p>Words go here.</p>
</div>

## 3 Missing Values

<div align="center">
  <img width="45%" alt="0a00005c.png" src="https://user-images.githubusercontent.com/53503018/136874866-9b5d89d0-5232-49ec-9cc7-f6f16eaa1c74.png">
  <img width="45%" alt="0b00000missing_na_b.png" src="https://user-images.githubusercontent.com/53503018/136874867-819e426b-bc9a-4b7c-8842-66f9d2b324b4.png">
  <img width="45%" alt="0c00005e.png" src="https://user-images.githubusercontent.com/53503018/136874870-16b44c0a-0cf8-48a9-8419-5ae742a3ea8f.png">

  <p>Words go here.</p>
</div>

## 4 Missing Questions

<div align="center">
  <img width="45%" alt="2scd.png" src="https://user-images.githubusercontent.com/53503018/136874948-3ac63d50-4c18-4579-99be-fd7f5190efae.png">
  <img width="45%" alt="2sce.png" src="https://user-images.githubusercontent.com/53503018/136874956-4564c8f0-c9df-41a4-a0b7-478e9c4fce2e.png">
  <img width="45%" alt="2missing_rels.png" src="https://user-images.githubusercontent.com/53503018/136874947-b975888d-e8db-4ed5-b5d1-e597ee08c5be.png">

  <p>Words go here.</p>
</div>

## 5 Missing Questions Pt. 2

<div align="center">
  <img width="45%" alt="3sch.png" src="https://user-images.githubusercontent.com/53503018/136875029-65aaf7bb-8dff-4ba1-aefc-29cf462a7e31.png">
  <img width="45%" alt="3sci.png" src="https://user-images.githubusercontent.com/53503018/136875031-9cb46e4a-b6f5-4c66-a352-e15760a68417.png">
  <img width="45%" alt="3scg.png" src="https://user-images.githubusercontent.com/53503018/136875028-98f4e0b5-48d5-4d84-a1e2-936fb53e3421.png">
  <img width="45%" alt="3scf.png" src="https://user-images.githubusercontent.com/53503018/136875026-18af4569-b990-4517-8308-896880e85ed3.png">

  <p>Words go here.</p>
</div>

## 6 Bars

<div align="center">
  <img width="45%" alt="Abortion Stances by Hispanic" src="https://user-images.githubusercontent.com/53503018/136875278-62288e2a-bb64-4050-b18f-8e8cda697c60.png">
  <img width="45%" alt="Abortion Stances by Party Bar" src="https://user-images.githubusercontent.com/53503018/136875282-647b6164-3f6b-4105-81cc-70a24c2c79e3.png">
  <img width="45%" alt="Abortion Stances by Party Bar 2" src="https://user-images.githubusercontent.com/53503018/136875280-eb7cfd80-e46b-450e-80b9-32ff357d3efa.png">
  <img width="45%" alt="Abortion Stances by Sex" src="https://user-images.githubusercontent.com/53503018/136875284-652698de-b7c2-4da2-8fe4-34b5c8c81e62.png">

  <p>Words go here.</p>
</div>

## 7 Correlations

<div align="center">
  <img width="45%" alt="1Abortion Stances by Party.png" src="https://user-images.githubusercontent.com/53503018/136875123-f6b1b241-cb3f-4b3c-9828-d4038137fac3.png">
  <img width="45%" alt="1Abortion Stances by Religious Activity.png" src="https://user-images.githubusercontent.com/53503018/136875124-247a4bf0-752d-448c-bacd-f1a10c0b99ae.png">
  <img width="45%" alt="1Abortion Stances by Education.png" src="https://user-images.githubusercontent.com/53503018/136875120-d9332ba1-408f-40c9-bc43-37d9c1840f36.png">
  <img width="45%" alt="1Abortion Stances by Age.png" src="https://user-images.githubusercontent.com/53503018/136875117-1bbdb8b5-8beb-4a3a-b494-473410d81c59.png">

  <p>Words go here.</p>
</div>

## 8 Time

<div align="center">
  <img width="45%" alt="Abortion Stances by Year" src="https://user-images.githubusercontent.com/53503018/136875293-45133031-3bf2-413f-9bd2-db91f33d4454.png">
  <img width="45%" alt="Abortion Stances by Sex over Time" src="https://user-images.githubusercontent.com/53503018/136875290-c6ec8ef8-422f-4f96-bb98-dcf7868c79ba.png">
  <img width="45%" alt="Abortion Stances by Party over Time" src="https://user-images.githubusercontent.com/53503018/136875289-8fa623f7-eeda-4c00-9806-cc2440835648.png">

  <p>Words go here.</p>
</div>
