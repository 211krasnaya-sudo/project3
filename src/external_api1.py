import os
from src.utils import convert_to_rub


def get_transaction_amount(transaction: dict) -> float:
    """Функция для получения суммы транзакции в рублях."""
    try:
        amount = float(transaction.get('amount', 0))
        currency = transaction.get('currency', 'RUB').upper()

        if currency == 'RUB':
            return amount
        elif currency in ['USD', 'EUR']:
            return convert_to_rub(amount, currency)
        else:
            print("Неизвестная валюта. Возвращаем сумму в исходной валюте.")
            return amount

    except (ValueError, TypeError):
        return 0.0
