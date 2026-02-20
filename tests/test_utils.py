import sys
import unittest
from typing import Any
from unittest.mock import mock_open, patch

import requests
import requests_mock


from src.utils import get_transaction_amount, transactions_tot

sys.path.insert(0, 'path_to_widget/src')


class TestUtils(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_transactions_tot(self, mock_file: Any) -> None:
        result = transactions_tot('data/operations_api.json')
        print(result)
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='not a json')
    def test_transactions_tot_invalid_json(self, mock_file: Any) -> None:
        result = transactions_tot('data/operations_api.json')
        self.assertEqual(result, [])

    @patch('src.utils.os.path.exists', return_value=False)
    def test_transactions_tot_file_not_found(self, mock_exists: Any) -> None:
        result = transactions_tot('data/operations_api.json')
        self.assertEqual(result, [])


class TestExternalAPI(unittest.TestCase):
    @patch('src.external_api1.convert_to_rub')
    def test_get_transaction_amount_usd(self, mock_convert_to_rub: Any) -> None:
        with requests_mock.Mocker() as m:
            m.register_uri('GET', 'https://api.apilayer.com/exchangerates_data/', text='data')
            response = requests.get('https://api.apilayer.com/exchangerates_data/')
            assert response.text == 'data'

    @patch('src.external_api1.convert_to_rub')
    def test_get_transaction_amount_eur(self, mock_convert_to_rub: Any) -> None:
        with requests_mock.Mocker() as m:
            m.register_uri('GET', 'https://api.apilayer.com/exchangerates_data/', text='data')
            response = requests.get('https://api.apilayer.com/exchangerates_data/')
            assert response.text == 'data'

    def test_get_transaction_amount_rub(self) -> None:
        transaction_data = {
            'id': 125,
            'amount': 1000.50,
            'currency': 'RUB'
        }
        result = get_transaction_amount(transaction_data)

        # Проверка, что результат соответствует ожидаемому
        self.assertEqual(result, 1000.50)

    def test_get_transaction_amount_unknown_currency(self) -> None:
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
