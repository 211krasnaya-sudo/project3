import json
import os
from typing import Union

from src.external_api1 import convert_to_rub


def transactions_tot(file_path: str) -> list[dict]:
    """Загружает транзакции из JSON-файла."""
    try:
        if not os.path.exists(file_path):
            return []

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:
                return []
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError("Файл JSON не корректен", e.doc, e.pos)
    except ValueError:
        raise ValueError("Не удалось преобразить число")
    except Exception as e:
        raise Exception(f"Это общее исключение{e}")


def get_transaction_amount(transaction: dict) -> Union[float, None]:
    """Функция для получения суммы транзакции в рублях."""
    try:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == 'RUB':
            return float(amount)
        elif currency in ['USD', 'EUR']:
            return convert_to_rub(amount, currency)
        else:
            print("Неизвестная валюта. Возвращаем сумму в исходной валюте.")
            return float(amount)

    except (ValueError, TypeError):
        raise ValueError("Не удалось преобразить число")


transaction_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}
if __name__ == '__main__':
    amount_in_rubles = get_transaction_amount(transaction_data)
    print(f"Сумма транзакции: {amount_in_rubles:.2f} руб.")
