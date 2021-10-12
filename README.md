# Writeup

## 1 Choosing a dataset to explore

I found https://vincentarelbundock.github.io/Rdatasets/articles/data.html which allowed me to sort by number or rows and columns. At this point I chose my data based on the percieved "richness" of the data. So I sorted by rows and looked through a few csvs until I found one that had a good amount of columns that seemed to encode distinct information (as opposed to very similar or the same information).

## 2 Data Parsing

The first step of this was to clean the data. I had some parsing issues, and many missing values. Some of the missing values were due to parsing issues which I solved.

<div align="center">
  <img height="300" alt="a" src="https://user-images.githubusercontent.com/53503018/136717881-14b7d002-cada-4171-ad32-cdaab5aa4298.png">
  <img height="300" alt="b" src="https://user-images.githubusercontent.com/53503018/136717883-aa207ceb-00b2-4259-bd9d-8323d594e036.png">
  <p>Parsing issues and missing values.</p>
</div>

## 2.5 Data Cleaning

A lot of the missing values besides `a` and `b` were an absence of opinions on aborition data, which we don't want bc that's the point so I removed rows that had miissing vlues for a gneneral opinoin on abortion and it helped. It was ok for missing vvalues for `a` and `b` because that just means "maybe" or "unknown" but it is auxiliary? data - not necessary for what we are measuring. would be nice if it was more tho.

<div align="center">
  <img width="45%" alt="d" src="./img/0_a00005c.png">
  <img width="45%" alt="e" src="./img/0_b00000missing_na_b.png">

  <p>Missing values before and after removing rows with <code>NA</code> for <code>ab_any</code></p>
</div>

## 3 R

<div align="center">
  <img height="300" alt="rsca.png" src="./img/r_sca.png">
  <img height="300" alt="rscb.png" src="./img/r_scb.png">
  <img height="300" alt="rscc.png" src="./img/r_scc.png">

  <p>Words go here.</p>
</div>

## 4 Missing Values

<div align="center">
  <img width="45%" alt="0a00005c.png" src="./img/0_a00005c.png">
  <img width="45%" alt="0b00000missing_na_b.png" src="./img/0_b00000missing_na_b.png">
  <img width="45%" alt="0c00005e.png" src="./img/0_c00005e.png">

  <p>Words go here.</p>
</div>

## 5 Missing Questions

<div align="center">
  <img width="45%" alt="2scd.png" src="./img/2_scd.png">
<img width="45%" alt="2sce.png" src="./img/2_sce.png">
<img width="45%" alt="2missing_rels.png" src="./img/2_missing_rels.png">

  <p>Words go here.</p>
</div>

## 6 Missing Questions Pt. 2

<div align="center">
  <img width="45%" alt="3sch.png" src="./img/3_sch.png">
<img width="45%" alt="3sci.png" src="./img/3_sci.png">
<img width="45%" alt="3scg.png" src="./img/3_scg.png">
<img width="45%" alt="3scf.png" src="./img/3_scf.png">

  <p>Words go here.</p>
</div>

## 7 Correlations

<div align="center">
  <img width="45%" alt="1Abortion Stances by Party.png" src="./img/1_Abortion Stances by Party.png">
<img width="45%" alt="1Abortion Stances by Religious Activity.png" src="./img/1_Abortion Stances by Religious Activity.png">
<img width="45%" alt="1Abortion Stances by Education.png" src="./img/1_Abortion Stances by Education.png">
<img width="45%" alt="1Abortion Stances by Age.png" src="./img/1_Abortion Stances by Age.png">

  <p>Words go here.</p>
</div>
