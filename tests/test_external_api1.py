import unittest
from unittest.mock import patch
from src.external_api1 import get_transaction_amount

class TestGetTransactionAmount(unittest.TestCase):

    @patch('src.utils.convert_to_rub', return_value=75.0)  # Замокируем convert_to_rub
    def test_get_transaction_amount_usd(self, mock_convert_to_rub):
        transaction_data = {
            'id': 123,
            'amount': 1000.50,
            'currency': 'USD'
        }

        result = get_transaction_amount(transaction_data)

        # Проверка, что результат соответствует ожидаемому
        self.assertEqual(result, 75.0)

        # Убедитесь, что convert_to_rub был вызван с правильными аргументами
        mock_convert_to_rub.assert_called_once_with('1000.5', 'USD')

    @patch('src.utils.convert_to_rub', return_value=85.0)  # Замокируем convert_to_rub
    def test_get_transaction_amount_eur(self, mock_convert_to_rub):
        transaction_data = {
            'id': 124,
            'amount': 1000.50,
            'currency': 'EUR'
        }

        result = get_transaction_amount(transaction_data)

        # Проверка, что результат соответствует ожидаемому
        self.assertEqual(result, 85.0)

        # Убедитесь, что convert_to_rub был вызван с правильными аргументами
        mock_convert_to_rub.assert_called_once_with('1000.5', 'EUR')

    def test_get_transaction_amount_rub(self):
        transaction_data = {
            'id': 125,
            'amount': 1000.50,
            'currency': 'RUB'
        }

        result = get_transaction_amount(transaction_data)

        # Проверка, что результат соответствует ожидаемому
        self.assertEqual(result, 1000.50)

    def test_get_transaction_amount_unknown_currency(self):
        transaction_data = {
            'id': 126,
            'amount': 1000.50,
            'currency': 'JPY'  # Неизвестная валюта
        }

        result = get_transaction_amount(transaction_data)

        # Проверка, что результат соответствует ожидаемому
        self.assertEqual(result, 1000.50)

if __name__ == '__main__':
    unittest.main()