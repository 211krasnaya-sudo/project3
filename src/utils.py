import json
import os
from src.external_api1 import convert_to_rub


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
        raise ValueError("Не удалось преобразить число")
    except Exception as e:
        raise Exception(f"Это общее исключение{e}")


def get_transaction_amount(transaction: dict) -> float:
    """Функция для получения суммы транзакции в рублях."""
    try:
        amount = str(transaction.get('amount', 0))
        currency = transaction.get('currency', 'RUB').upper()

        if currency == 'RUB':
            return float(amount)
        elif currency in ['USD', 'EUR']:
            return convert_to_rub(amount, currency)
        else:
            print("Неизвестная валюта. Возвращаем сумму в исходной валюте.")
            return float(amount)

    except (ValueError, TypeError):
        raise ValueError("Не удалось преобразить число")


    # Пример использования функции
transaction_data = {
        'id': 123,
        'amount': 1000.50,
        'currency': 'USD'
    }
if __name__ == '__main__':
    amount_in_rubles = get_transaction_amount(transaction_data)
    print(f"Сумма транзакции: {amount_in_rubles:.2f} руб.")
