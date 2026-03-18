import json
import csv
from typing import List, Dict, Any

import pandas as pd
from src.transactions_post import process_bank_search, process_bank_operations


def transactions_tot(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def reding_transactions_csv(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        return [row for row in reader]


def reding_transactions_excel(file_path: str) -> List[Dict[str, Any]]:
    reader = pd.read_excel(file_path)
    return reader.to_dict(orient="records")


def main():
    # global transactions
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice_user = input("Пользователь: ")
    if choice_user not in {'1', '2', '3'}:
        print("Недопустимый выбор. Попробуйте снова.")
        return

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

    status_options = ["executed", "canceled", "pending"]

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").strip().lower()
        if status in status_options:
            print(f"Операции отфильтрованы по статусу '{status.upper()}'")
            filtered_transactions = [t for t in transactions if t['state'].lower() == status]
            break
        else:
            print(f"Статус операции '{status.upper()}' недоступен. Попробуйте снова.")

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

    # Поиск по описанию
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
