import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
BASE_URL = "https://api.apilayer.com/exchangerates_data/"

def convert_to_rub(amount, currency):
    """Конвертирует сумму в рубли с использованием внешнего API."""
    if currency not in ['RUB', 'USD', 'EUR']:
        raise ValueError('Unsupported currency')

    if currency == 'RUB':
        return float(amount)

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {
        "apikey": API_TOKEN
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Отслеживаем ошибки при запросе

    data = response.json()
    return float(data['result'])
