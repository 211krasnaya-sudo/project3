import json
from typing import List, Dict, Any
from data import operations_api, transaction_csv, transaction_excel
from src.transactions_post import process_bank_search
from src.transactions_csv_excel import reading_transaction_csv, reading_transaction_excel
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.transactions_post import process_bank_search
import pandas as pd


def transactions_tot(full_path: str) -> List[Dict[str, Any]]:
    """ Загружает данные из JSON-файла и преобразует в унифицированный формат. """
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return [
        {
            'id': op.get('id'),
            'state': op.get('state'),
            'date': op.get('date'),
            'amount': op.get('operationAmount', {}).get('amount', ''),
            'currency_name': op.get('operationAmount', {}).get('currency', {}).get('name', ''),
            'currency_code': op.get('operationAmount', {}).get('currency', {}).get('code', ''),
            'from': op.get('from', ''),
            'to': op.get('to', ''),
            'description': op.get('description')
        }
        for op in data if op
    ]

def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
    """Получает и валидирует выбор пользователя."""
    while True:
        user_input = input(f"{prompt}\nПользователь: ").strip().lower()
        for choice in valid_choices:
            if user_input == choice.lower():
                return choice
        print(f"Некорректный ввод. Пожалуйста, выберите один из вариантов: {', '.join(valid_choices)}")


def filter_rub_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Фильтрует транзакции, оставляя только рублевые."""
    return [t for t in transactions if t.get("currency_code") == "RUB"]


def print_transaction(transaction: Dict[str, Any]) -> None:
    """Форматирует и печатает информацию о транзакции в заданном формате."""
    date = get_date(transaction["date"])
    description = transaction["description"]

    # Обработка from и to
    from_account = mask_account_card(transaction["from"]) \
        if "from" in transaction and isinstance(transaction["from"], str) else "Не указано"
    to_account = mask_account_card(transaction["to"]) \
        if "to" in transaction and isinstance(transaction["to"], str) else "Не указано"

    # Получаем сумму и валюту
    amount = transaction["amount"]
    currency = transaction["currency_name"]

    # Формируем строку перевода
    transfer_line = ""
    if from_account != "Не указано" and to_account != "Не указано":
        transfer_line = f"{from_account} -> {to_account}"
    elif to_account != "Не указано":
        transfer_line = f"{to_account}"

    # Печатаем информацию о транзакции
    print(f"{date} {description}")
    if transfer_line:
        print(transfer_line)
    print(f"Сумма: {amount} {currency}\n")

def reading_transaction_csv_v1(file_path: str, delimiter: str = ";") -> List[dict]:

    """Функция считывает финансовые операции из CSV-файла."""
    try:
        reader = pd.read_csv(file_path, delimiter=delimiter)
        return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден!")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла {e}")
        return []


def reading_transaction_excel_v1(file_path: str) -> list[dict]:
    """Функция считывает финансовые операции из EXCEL-файла."""
    try:
        reader = pd.read_excel(file_path)
        return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении EXCEL-файла {e}")
        return []


def main():
    while True:
        print(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла.\n"
        )
    # Получаем выбор пользователя
    choice_user = input("Пользователь: ").strip()
    if choice_user not in {'1', '2', '3'}:
        print("Недопустимый выбор. Попробуйте снова.")
        return
    # Определяем путь к файлу
    transactions = []
    file_path = input("Введите путь к файлу: ")
    if choice_user == '1':
        transactions = transactions_tot(file_path)
    elif choice_user == '2':
        transactions = reding_transactions_csv(file_path)
    elif choice_user == '3':
        transactions = reding_transactions_excel(file_path)

    if not transactions:
        print("Не найдено транзакций.")
        return
    # Фильтрация по статусу
    status_options = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").strip().lower()
        if status in status_options:
            print(f"Операции отфильтрованы по статусу '{status.upper()}'")
            filtered_transactions = [t for t in transactions if t['state'].lower() == status]
            break
        else:
            print(f"Статус операции '{status.upper()}' недоступен. Попробуйте снова.")

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower() == 'да'
    if sort_choice:
        order_choice = input("Сортировать по возрастанию или по убыванию? ").strip().lower()
        if order_choice == 'по возрастанию':
            filtered_transactions.sort(key=lambda t: t['date'])
        elif order_choice == 'по убыванию':
            filtered_transactions.sort(key=lambda t: t['date'], reverse=True)

    # Фильтрация только по рублевым транзакциям
    ruble_only = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower() == 'да'
    if ruble_only:
        filtered_transactions = [t for t in filtered_transactions if
                                 t['currency_name'] == 'руб.' or t['currency_code'] == 'RUB']

    # Поиск по ключевому слову
    description_search = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower() == 'да'
    if description_search:
        search_str = input("Введите слово для поиска: ")
        filtered_transactions = process_bank_search(filtered_transactions, search_str)

    # Вывод результатов
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(
                f"{transaction['date']} {transaction['description']}\nСчет **{transaction['from'][-4:]}\nСумма: {transaction['amount']} {transaction['currency_name'] if 'currency_name' in transaction else transaction['currency_code']}\n")


if __name__ == '__main__':
    main()
