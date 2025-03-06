import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def amount_transition(transition: dict) -> float:
    """Фукция обрабатывает транзакцию и возвращает её сумму в рублях"""
    code = transition["operationAmount"]["currency"]["code"]
    print(code)
    if code != "RUB":
        amount = transition["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

        payload = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.json())
        print(response.json()["result"])
        return response.json()["result"]
    else:
        return transition["operationAmount"]["amount"]
