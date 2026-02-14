import json
import os
from typing import Dict, List
from dotenv import load_dotenv
from typing import Optional
import requests


load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
BASE_URL = "https://api.apilayer.com/exchangerates_data/"


def transactions_tot(file_path: str) -> list[dict]:
    """Загружает транзакции из JSON-файла."""
    try:
        #Проверяем существование файла
        if not os.path.exists(file_path):
            return []
        #Открыть и прочитать файл
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            #Проверка форматирования
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:   #Иначе возвращается пустой список
                return []
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Файл JSON не корректен")
    except ValueError:
        raise ValueError("Не удалось преобразить сумму в число")
    except Exception as e:
        raise Exception(f"Это общее исключение{e}")


def convert_to_rub(amount: str, currency: str) -> Optional[float]:
    """Конвертирует сумму в рубли с использованием внешнего API."""
    if currency not in ['RUB', 'USD', 'EUR']:
        raise ValueError('Unsupported currency')

    if currency == 'RUB':
        return float(amount)


    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {
        "apikey": API_TOKEN
    }

    response = requests.get(url, headers=headers, data={})
    response.raise_for_status()  # Отслеживаем ошибки при запросе

    data = response.json()
    return float(data.get('result'))
