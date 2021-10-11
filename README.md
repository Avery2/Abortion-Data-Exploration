# Writeup

I explored...

## Choosing a dataset to explore

I intially had difficulty 

I found https://vincentarelbundock.github.io/Rdatasets/articles/data.html which allowed me to sort by number or rows and columns. At this point I chose my data based on the percieved "richness" of the data. So I sorted by rows and looked through a few csvs until I found one that had a good amount of columns that seemed to encode distinct information (as opposed to very similar or the same information).

## Data Parsing and Cleaning

The first step of this was to clean the data. I had some parsing issues, and many missing values. Some of the missing values were due to parsing issues which I solved.

<div align="center">
  <img height="300" alt="a" src="https://user-images.githubusercontent.com/53503018/136717881-14b7d002-cada-4171-ad32-cdaab5aa4298.png">
  <img height="300" alt="b" src="https://user-images.githubusercontent.com/53503018/136717883-aa207ceb-00b2-4259-bd9d-8323d594e036.png">
  <p>Parsing issues and missing values.</p>
</div>

A lot of the missing values besides `a` and `b` were an absence of opinions on aborition data, which we don't want bc that's the point so I removed rows that had miissing vlues for a gneneral opinoin on abortion and it helped. It was ok for missing vvalues for `a` and `b` because that just means "maybe" or "unknown" but it is auxiliary? data - not necessary for what we are measuring. would be nice if it was more tho.

<div align="center">
  <img width="45%" alt="d" src="./missing_na_a.png">
  <img width="45%" alt="e" src="./missing_na_b.png">

  <p>Missing values before and after removing rows with <code>NA</code> for <code>ab_any</code></p>
</div>

Wrote to csv.

## Initial Visualizations

Tablaue
