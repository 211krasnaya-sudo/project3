import requests

from src.utils import API_KEY


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из указанной валюты в рубли, используя API.
    """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return float(data["result"])
    else:
        print(f"Ошибка при запросе к API: {response.status_code} - {response.text}")
        return 0.0
