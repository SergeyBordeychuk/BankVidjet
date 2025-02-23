import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def amount_transition(transition: dict) -> float:
    code = transition["operationAmount"]["currency"]["code"]
    if code == "RUS":
        return transition["operationAmount"]["amount"]
    amount = transition["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

    payload = {}
    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()["result"]
