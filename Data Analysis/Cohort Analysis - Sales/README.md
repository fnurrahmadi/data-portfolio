# Cohort Analysis - Sales

An online retail (e-commerce) store sells gifts and homewares for adults and children through their website. As a new store that has only been logging their sales data for several months, they have just started performing analysis on their existing data. One of their concerns is related to their customer groups since they have run different campaigns and released new products over the months, and they would like to see how their customer groups are affected. As such, a cohort analysis is done in attempt to understand the effect on their customer groups over time.

## Getting the Data

The data is obtained from Kaggle [here](https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business).

## Formatting the Data

- Open the csv data as an Excel File.
- Convert the csv formatted data into a table by performing Text to columns with the delimiter set to commas.
- Highlight the Date column and perform another Text to columns to set the date format as MDY.

## Creating Cohort Groups

- Create a pivot table on a new worksheet where the Row is set to CustomerNo and the Values is set to Min of Date.
- On the master table, create a new column named CohortGroup and use VLOOKUP to grab the Min of Date using CustomerNo as the reference.
- Format the CohortGroup column so that it only shows the month and year.
- Create a new column called month, where it calculates the rounded difference of the CohortGroup cell and the Date cell.

## Performing the Cohort Analysis

- Create a new pivot table on a new worksheet as such:
    - Rows: Year and Month from CohortGroup
    - Columns: month
    - Values: Sum of Price
- Set the Design > Report Layout to Tabular Form and also set Repeat All Item Labels.
- Highlight all the Values > click Home > Conditional Formatting > Color Scales > choose a suitable color format.

## What can we take away from the cohort analysis?
- It seems that the 2018 Dec cohort, the oldest cohort out of all, are contributing the most sales over time.
- The 2019 Aug cohort in particular is performing the worst out all.
- Based on their average, cohorts 2019 Apr, May, Jun, Jul, and Aug are the worst contributors over time.
- Unlike all the other cohorts, cohort 2019 Dec is performing quite bad in their first month.
- The latest sales which is Dec 2019 are not doing well in all cohorts but 2018 Dec, which is concerning.

All of the above are key points which can be further drilled down in an analysis for another day :)
