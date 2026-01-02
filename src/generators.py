from binascii import Error
from typing import Generator, Iterator

import pytest


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """Функция фильтрует трансакции, где валюта операции соответствует заданной("USD")."""
    for transaction in transactions:

        if transaction == "Error":
            raise ValueError("В списке словарей нет кода валют")

        # Проверяем наличие ключа 'currency' и его соответствие заданной валюте
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """ Генератор, возвращающий описание каждой транзакции. """
    for i in transactions:
        if "description" in i:
            yield i["description"]


def card_number_generator(card_start: int, stop: int) -> Generator:
    for i in range(card_start, stop + 1):
        card_number = f"{i:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
