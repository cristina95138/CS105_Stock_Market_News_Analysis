# Project Phase 2 - Data Cleaning and EDA

## Datasets Used

Stock price dataset (Download):
https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs \
News headlines dataset (Download):
https://www.kaggle.com/aaron7sun/stocknews \

## EDA Process
For this phase we did sentiment analysis on headlines. We did this in two separate parts:

### Cristina

I first cleaned the data by deleting any null rows and converting all the headlines to strings and all the numbers to floats. The first analysis I did was seing the frequencies of all the values within each column. I then compared how different aspects of the news headlines sentiment had to do with an up or a down day for the stock. I then did two pair plots. The first with the raw data the the second with the regression data. The regression data was more readbale so it was easier to analyze. Finaly I did a parallel coordinates plot comparing the positivity, negativity, and neutrality of the news headline with wheteher it was an up or a down day for the stock. The analysis I did didn't reveal a lot, but I was able to get a small aount of useful information.


### Marcos
For EDA, I first cleaned the data. I ended up deleting only three rows. The first analysis I did was on the most popular topics in the headlines, I did this by counting the number of times a word appeared. Just to see what topics they were and if they stood out as being negative or positive. Then, I compared sentiment analysis between high scoring and low scoring headlines. The reason why I did this is to test my hypothesis that higher upvoted posts/headlines are most likely negative, since that is what usually captures peoples attention. Next I checked if the sentiment analysis of headlines had any correlation with the Dow Jones Industrial Average(DJIA). After that I did sentiment analysis on headlines containing particular topics. Through out the process I interweaved graphs, stats and comments on my findings.


## Summary of Findings

### Cristina

Something that was revealed within the data was that there isn't that much of a correlation between the positivity/negativity of the news and whether it is an up day or a down day. There is a slight edge in the market, however, when the news is negative. This slight edge being that the stock is slightly more likely to have an up day when the news is negative. I conclude from this that the stock has been down for a couple of days due to a couple days of bad news thus leading to a "discounted stock" that is more appealing to buy to investors. This increase in the amount of stcoks bought on that day would thus lead to an increase in the price of the stock. As for positive news, investors usually sell their stocks at a high, or when they think the stock is above its value. This then leads to a drop in the price of the stock due to a high frequency of sells. All in all, I believe that the news slightly effects the stock prices, but not that much. Many of the stock ups and downs are due to a majority of people just wanting to buy or sell based on the price. The stock market is just based off of the amount of stocks bought and sold, and not of news so it is logical to deduce that the news has no effect unless it directly has to do with that specific stock.

### Marcos

One thing we found out is that the sentiment analysis values of headlines and the DJIA are not correlated. As well as high and low upvoted headlines have similar sentiment analysis values. Though, this is not the case for topics like the US, North Korea, and war. All of which had slighly less negative sentiment values in the lower upvoted headlines.

## How to Run Code
Before running you must first download the following libraries(based on our machines, so you may not need to download them):

* nltk
* afinn

```
pip install nltk afinn
```
