import requests
import datetime
#from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = '?????????????????????'
auth_token = '????????????????????'

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": "??????????????"
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()


data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday = float(data_list[0]['4. close'])
before_yesterday = float(data_list[1]['4. close'])

difference = yesterday - before_yesterday

up_down_percent = round((difference / before_yesterday) * 100, 2)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator
news_params = {
    "apiKey": "???????????????????",
    "q": STOCK,
    "from": f"{datetime.date.today() - datetime.timedelta(days=3)}"
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)

three_articles = news_response.json()["articles"][0:3]
articles_formatted = [f"Headline:{article['title']}\nBrief:{article['description']}" for article in three_articles]
for article in articles_formatted:
    print(f"{STOCK}:{up_down} {up_down_percent}%\n{article}")


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

