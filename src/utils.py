import json
import os
from logging import exception
from typing import Union

from src.external_api1 import convert_to_rub
from src.logging_config import setup_logging

logger = setup_logging()

LOG_DIR = 'logs'
LOS_FILE_UTILS = os.path.join(LOG_DIR, 'utils.log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def transactions_tot(file_path: str, utils_loger=None) -> list[dict]:
    """Загружает транзакции из JSON-файла."""
    utils_loger.info(f"Загрузка трансакций из файла: {file_path}")
    try:
        if not os.path.exists(file_path):
            return []

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                utils_loger.info(f"Успешно загружено {len(data)} трансакций из файла {file_path}")
                return data
            else:
                utils_loger.warning(f"Файл {file_path} содержит данные не в формате списка. Возвращается пустой список")
                return []
    except json.JSONDecodeError as e:
        utils_loger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        raise json.JSONDecodeError("Файл JSON не корректен", e.doc, e.pos)
    except ValueError:
        utils_loger.error(f"Не удалось преобразить число в файле: {file_path}")
        raise ValueError("Не удалось преобразить число")
    except Exception as e:
        utils_loger.exception(f"Произошла ошибка при чтении файла: {exception}")
        raise Exception(f"Это общее исключение {e}")


def get_transaction_amount(transaction: dict, utils_loger=None) -> Union[float, None]:
    """Функция для получения суммы транзакции в рублях."""
    utils_loger.info(f"Запуск функции get_transaction_amount для получения суммы транзакции в рублях: {transaction}")
    try:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == 'RUB':
            utils_loger.info(f"Валюта равна рублям {transaction}.")
            return float(amount)
        elif currency in ['USD', 'EUR']:
            return convert_to_rub(amount, currency)
        else:
            utils_loger.warning(f"Неизвестная валюта. Возвращаем сумму в исходной валюте.")
            print("Неизвестная валюта. Возвращаем сумму в исходной валюте.")
            return float(amount)

    except (ValueError, TypeError) as e:
        utils_loger.exception(f"Не удалось преобразить число {e}.")
        raise ValueError("Не удалось преобразить число.")


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
