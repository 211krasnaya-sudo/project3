
from src.utils import convert_to_rub


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
