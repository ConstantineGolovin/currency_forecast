import requests
import pandas as pd

def load_currency_data(currency_code="USD"):
    """
    Загружает данные о курсе валют за последний месяц
    currency_code - код валюты (можно выбрать любую)
    """
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Ошибка загрузки данных")

    data = response.json()
    rate = data["Valute"][currency_code]["Value"]
    date = data["Date"]

    df = pd.DataFrame({"date": [date], "rate": [rate]})
    return df