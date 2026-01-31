import pytest
from unittest.mock import patch
from src.utils import transactions_total


# Тестовая функция
@pytest.mark.parametrize("transaction, expected", [
    ({"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}, 1000.0),
    ({"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}}, 75.0),  # Примерный курс
])
@patch('src.utils.get_exchange_rate')  # Подмена функции получения курса
def test_transactions_total(mock_get_exchange_rate, transaction, expected):
    # Настраиваем фейковый курс
    mock_get_exchange_rate.return_value = 75.0

    # Вызываем тестируемую функцию
    result = transactions_total(transaction)

    # Проверяем, что результат соответствует ожиданиям
    assert result == expected

