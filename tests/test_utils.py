import pytest
import unittest
from unittest.mock import patch, mock_open, MagicMock
from src.utils import load_transactions
from src import external_api
from src.external_api import convert_to_rub

class TestUtils(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_load_transactions(self, mock_file):
        from src.utils import load_transactions
        result = load_transactions('dummy_path')
        print(result)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='not a json')
    def test_load_transactions_invalid_json(self, mock_file):
        from src.utils import load_transactions
        result = load_transactions('dummy_path')
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=False)
    def test_load_transactions_file_not_found(self, mock_exists):
        from src.utils import load_transactions
        result = load_transactions('dummy_path')
        self.assertEqual(result, [])

class TestExternalAPI(unittest.TestCase):
    @patch('external_api.requests.get')
    def test_convert_to_rub(self, mock_get):
        from src.external_api import convert_to_rub
        mock_response = MagicMoc()
        mock_get.return_value.json.return_value = {'result': 75.0}
        mock_get.return_value.raise_for_status = lambda: None

        amount_in_rub = convert_to_rub(100, 'USD')
        self.assertEqual(amount_in_rub, 75.0)

    def test_convert_invalid_currency(self):
        from src.external_api import convert_to_rub
        mock_response = MagicMoc()
        with self.assertRaises(ValueError):
            convert_to_rub(100, 'JPY')

if __name__ == '__main__':
    unittest.main()