import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_KEY = "YOUR_ALPHAVANTAGE_API_KEY"
NEWS_KEY = "YOUR_NEWS_API_KEY"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price.
param_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}

response_stock = requests.get(STOCK_ENDPOINT, params=param_stock)
response_stock.raise_for_status()
stock_data = response_stock.json()

data_list = [value for (key,value) in stock_data["Time Series (Daily)"].items()]
yesterday_close = data_list[0]['4. close']


#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_close = data_list[1]["4. close"]


#TODO 3. - Find the positive difference between 1 and 2.
difference = abs(float(yesterday_close)-float(day_before_yesterday_close))


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = (difference/float(yesterday_close))*100



    ## STEP 2: https://newsapi.org/ 
    #Get the first 3 news pieces for the COMPANY_NAME. 

#TODO 5. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
param_news = {
    'apiKey': NEWS_KEY,
    'q': COMPANY_NAME
}
response_news = requests.get(NEWS_ENDPOINT, params=param_news)
response_news.raise_for_status()
news_data = response_news.json()


#TODO 6. - Use Python slice operator to create a list that contains the first 3 articles. 
articles = news_data['articles'][:3]
print(articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

account_id = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
client = Client(account_id, auth_token)


#TODO 7. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {articles[i]["title"]}. \nBrief: {articles[i]["description"]}" for i in range(len(articles))]


#TODO 8. - Send each article as a separate message via Twilio. 
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="YOUR_TWILIO_PHONE_NUMBER",
        to="YOUR_VERIFIED_PHONE_NUMBER"
    )
    print(message.status)



