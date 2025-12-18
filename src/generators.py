from typing import Iterator, Generator

import pytest

def filter_by_currency(transactions: list[dict], currency: str | None = "USD") -> Iterator:
    """Функция фильтрует трансакции, где валюта операции соответствует заданной("USD")."""
    for transaction in transactions:
        # Проверяем наличие ключа 'currency' и его соответствие заданной валюте
        if transaction.get('currency') == currency:
            yield transaction

            transactions = [
                {'amount': 100, 'currency': 'USD', 'description': 'Покупка'},
                {'amount': 200, 'currency': 'EUR', 'description': 'Оплата'},
                {'amount': 150, 'currency': 'USD', 'description': 'Перевод'},
                {'amount': 300, 'currency': 'RUB', 'description': 'Снятие'}
            ]

            # Создаем итератор для USD транзакций
            usd_transactions = filter_by_currency(transactions,'USD')

            # Проходим по результатам
            for tx in usd_transactions:
                print(tx)

def transaction_descriptions(transactions: list[dict]) -> None[str]:
    """ Генератор, возвращающий описание каждой транзакции. """
    for tx in transactions:
        yield tx.get("description", "")

def card_number_generator(start: int, end: int) -> Generator:
    card_number = "00000000000000000"
    x = start
    counter  = 0
    for i in range(int(end)) - int(start):
        counter = int(x)
        counter += 1
        x = str(counter)
        if len(x) < len(card_number):
            card_number = "0" * (len(card_number) - len(x)) + x
            form_num = card_number(card_number)
            print(form_num)

