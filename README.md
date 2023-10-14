# Visualizing-Earnings-Based-on-College-Majors

I'll be working with recent-grads.csv, based on a previously done project, a dataset on the job outcomes of students who graduated from college between 2010 and 2012. The original data on job outcomes was released by the American Community Survey, which conducts surveys and aggregates the data. 

Below are the definitions of the variables used:

Rank:	Rank by median earnings (the dataset is ordered by this column)
Major_code:	Major code, FO1DP in ACS PUMS
Major:	Major Description
Major_category:	Category of major from Carnevale et al
Total:	Total number of people with major
Sample_size:	Sample size (unweighted) of full-time, year-round ONLY (used for earnings)
Men:	Male graduates
Women:	Female graduates
ShareWomen:	Women as a share of total
Employed:	Number employed (ESR == 1 or 2)
Full_time:	Employed 35 hours or more
Part_time:	Employed less than 35 hours
Full_time_year_round:	Employed at least 50 weeks (WKW == 1) and at least 35 hours (WKHP >= 35)
Unemployed:	Number unemployed (ESR == 3)
Unemployment_rate:	Unemployed / (Unemployed + Employed)
Median:	Median earnings of full-time, year-round workers
P25th:	25th percentile of earnings
P75th:	75th percentile of earnings
College_jobs:	Number of jobs requiring a college degree
Non_college_jobs:	Number of jobs not requiring a college degree
Low_wage_jobs:	Number of low-wage service jobs
