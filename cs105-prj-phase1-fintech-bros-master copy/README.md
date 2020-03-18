# Project Phase 1 - Data Collection and Data Cleaning

## Datasets Used

Stock price dataset (Download):
https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs \
News headlines dataset (Download):
https://www.kaggle.com/aaron7sun/stocknews \
Additional headlines dataset (Web-Crawling):
We will be scraped from crawling the reddit news page (r/news) with the pushshift.io Reddit API (https://github.com/pushshift/api).

## Web-Crawler/Scraper Description 

Scrapes Reddit News Data

## Data Obtained

Stock price dataset provides the low, high, open and close price for a stock, the date that the prices were recorded and the volume. They’re all stocks traded on the NYSE, NASDAQ, and NYSE MKT.

News headlines dataset provides the top 25 headlines from /r/worldnews, a Reddit community where people post articles relating to news outside of the US. The dataset contains headlines from 2008-06-08 to 2016-07-01.

## How to Run Code

<strong> To run crawler </strong>

```
scrapy crawl articles
```

<strong> Terminal command to create data.csv file with the headlines of the posts: </strong>

```
scrapy crawl articles -o data.csv
```
