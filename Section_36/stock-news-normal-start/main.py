from email import message
from http import client
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API_KEY = "MA9RVP6JGD9510MD"
NEWS_API_KEY = "07715f7bf2ca4581875fecbb734a358a"
TWILIO_SID = "ACfacd30e6cb9206c96f45b61d0bc3e400"
TWILIO_AUTH_TOKEN = "65276ef9390dd47f4350da81786c3a5d"
TWILIO_PHONE_NUMBER = "+19133575475"


DAILY_STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY,
}


def get_stock_prices():
    response = requests.get(STOCK_ENDPOINT, params=DAILY_STOCK_PARAMS)
    response.raise_for_status()
    data = response.json()
    stock_data = data["Time Series (Daily)"]
    stock_prices = [value for (key, value) in stock_data.items()]
    return stock_prices


def get_percentage_difference(yesterday_stock_price, day_before_yesterday_stock_price):
    positive_difference = abs(
        float(yesterday_stock_price["4. close"])
        - float(day_before_yesterday_stock_price["4. close"])
    )
    percentage_difference = (
        positive_difference / float(yesterday_stock_price["4. close"])
    ) * 100
    return percentage_difference


def get_news():
    NEWS_PARAMS = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    response.raise_for_status()
    data = response.json()
    articles = data["articles"]
    first_three_articles = articles[:3]
    formatted_articles = [
        f"{STOCK_NAME}: {percentage_difference}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in first_three_articles
    ]

    return formatted_articles


stock_price_data = get_stock_prices()
percentage_difference = get_percentage_difference(
    stock_price_data[0], stock_price_data[1]
)

print(percentage_difference)

if percentage_difference > 3:
    first_three_articles = get_news()
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=first_three_articles, from_=TWILIO_PHONE_NUMBER, to="+84905901869"
    )
else:
    print("No News")
