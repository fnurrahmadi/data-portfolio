# [Jakarta Open Data](https://datastudio.google.com/reporting/18b51ab4-5b0f-4f1b-a0ef-587bd8203399/page/huv4C)

Jakarta Open Data is a web portal created by the government to supply accessible data pertaining to the populace of Jakarta. In this particular project, I acquired data related to population and created a dashboard using Google Data Studio.

What sort of information can the dashboard show?
- Average family registries per year
- Average number of sub-districts, hamlets, and neighborhoods in a district per year
- Trend of family registries per year
- All of the above but with the use of filter by year, sub-city, and district

What sort of questions would try I answering using this dashboard?
- Is there a significant change in numbers when a new governor gets elected?
- Is there a significant change in numbers when [insert event] takes place in that year compared to the previous year? (for example: the news of capital city change)
- etc

Click below to see the dashboard right away

[Link to Dashboard - Google Data Studio](https://datastudio.google.com/reporting/18b51ab4-5b0f-4f1b-a0ef-587bd8203399/page/huv4C)

## Getting the Data

The data can be accessed and downloaded from the website directly from this link: https://data.jakarta.go.id/ in the form of either json or tabular data. I gathered population data from 2011 to 2019 in json format. The data consists of columns such as the year of the record, the sub-city, the district, the sub-district, the number of hamlets, the number of neighborhoods, and the number of family registries.

## Joining the Data

Since the data comes in different files, all the json files are read and appended into one dataframe using pandas. Assume that all data are unclean, the data values are checked for their daata types and uniqueness and stripped for extra spaces, to ensure the quality of the results in the end product -- the dashboard. Once the quality of data is ensured, the clean data is exported into one file, ready to be uploaded.

## Uploading the Data

Using gspread, the data is uploaded into a Google Sheets file that is stored within Google Drive. The upload process uses a separate credential file to make sure that the Drive and its components are kept safe -- and obviously the credential file is also not uploaded here on github. The method that which the upload process executes is to overwrite all the rows on the Google Sheets file each time an update is run.

## Dashboard

The Google Data Studio dashboard reads its data from the Google Sheets file. The question is -- what information are you looking to find from the data?
