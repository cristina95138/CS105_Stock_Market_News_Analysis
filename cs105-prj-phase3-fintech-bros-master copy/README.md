# Project Phase 3 - Data Analysis Phase

## Datasets Used

Stock price dataset (Download):
https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs \
News headlines dataset (Download):
https://www.kaggle.com/aaron7sun/stocknews

# Hypothesis and Questions

Will the a positive news sentiment increase the stock price, and will a negative news sentiment decrease the stock price? \
  The positive news sentiment will increase the stock price, but the negative nws sentiment will increase the stock price as well. Like what was revealed in phase two, there's no real rhyme or reason when it comes to stock prices.
  
Does news at least have a slight effect on stock prices? \
  I believe it does, but it doesn't matter if it's postitive or negative. Like with the recent CoronaVirus headlines, even though the stock is dropping a lot, there are still up days even when the news is negative.

# Summary of the Data Analysis Process Performed

I first cleaned the data by deleting any null rows and converting all the headlines to strings and all the numbers to floats. The first analysis I did was seeing which news sentiment variables and stock price variables were correlated. I then found what the coefficients were various words within the news articles. I looked at what the words with the highest coefficients and the lowest coefficients. I then tested various machine learning models on the data set to see which one was the most accurate. The analysis I did didn't reveal a lot, but I was able to get a small amount of useful information. 

# Results and Observations Obtained

Something that was revealed within the data was that there isn't that much of a correlation between the positivity/negativity of the news and whether it is an up day or a down day. There is a slight edge in the market, however, when the news is negative. This slight edge being that the stock is slightly more likely to have an up day when the news is negative. I conclude from this that the stock has been down for a couple of days due to a couple days of bad news thus leading to a "discounted stock" that is more appealing to buy to investors. This increase in the amount of stcoks bought on that day would thus lead to an increase in the price of the stock. As for positive news, investors usually sell their stocks at a high, or when they think the stock is above its value. This then leads to a drop in the price of the stock due to a high frequency of sells. All in all, I believe that the news slightly effects the stock prices, but not that much. Many of the stock ups and downs are due to a majority of people just wanting to buy or sell based on the price. The stock market is just based off of the amount of stocks bought and sold, and not of news so it is logical to deduce that the news has no effect unless it directly has to do with that specific stock.

Will the a positive news sentiment increase the stock price, and will a negative news sentiment decrease the stock price? \
  The positive news sentiment did increase the stock price, but the negative nws sentiment increased the stock price as well.

Does news at least have a slight effect on stock prices? \
  Yes, but there is no difference between very negative news and vey positive news.

# How to Run Code

On an IDE that can run Python. Like Junyper Notebook or JunyperLab.
