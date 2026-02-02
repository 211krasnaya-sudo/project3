import os
from dotenv import load_dotenv
from pathlib import Path
from src.external_api import convert_to_rub


load_dotenv()
current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir / 'data' / 'operations.json'
API_KEY = os.getenv('API_KEY')


def transactions_total(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount
    else:
        return convert_to_rub(amount, currency)
