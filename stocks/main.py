import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
HEADERS = {"Content-Type": "application/json"}
NEWS_API = os.getenv("NEWS_API")
NEWS_API_URL = "https://newsapi.org/v2/everything"
ALPHA_ADV_API = os.getenv("ALPHA_ADV_API")
ALPHA_ADV_URL = "https://www.alphavantage.co/query"
FUNCTION = "TIME_SERIES_DAILY"
STOCK = "AMD"

parameters_alpha = {

    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": ALPHA_ADV_API,

}

parameters_news = {

    "q": STOCK,
    "apikey": NEWS_API,

}

def get_stock_differential():
    request_alpha = requests.get(ALPHA_ADV_URL, params=parameters_alpha)
    data_alpha = request_alpha.json()
    time_series = data_alpha["Time Series (Daily)"]
    available_dates = list(time_series.keys())
    yesterdays_close = float(data_alpha["Time Series (Daily)"][available_dates[0]]["4. close"])
    day_before_close = float(data_alpha["Time Series (Daily)"][available_dates[1]]["4. close"])
    close_differential_points = yesterdays_close - day_before_close
    close_differential_percent = (close_differential_points / yesterdays_close) * 100
    return close_differential_percent

def get_news():
    request_news = requests.get(NEWS_API_URL, params=parameters_news)
    data_news = request_news.json()

    top_three_stories = {data_news["articles"][0]["title"]: data_news["articles"][0]["description"],
                         data_news["articles"][1]["title"]: data_news["articles"][1]["description"],
                         data_news["articles"][2]["title"]: data_news["articles"][2]["description"],

    }
    return top_three_stories

def send_discord_update():
    top_three_stories = get_news()
    close_differential_percent = round(get_stock_differential(), 2)

    news_text = ""
    for title, description in top_three_stories.items():
        news_text += f"**{title}**\n{description}\n\n"

    message = {"content": f"{STOCK} is {close_differential_percent}%\n"
                          f"{news_text}"
               }

    requests.post(DISCORD_WEBHOOK, json=message, headers=HEADERS)

close_differential_percent = get_stock_differential()
if abs(close_differential_percent) > 10:
    send_discord_update()
