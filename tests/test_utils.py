import unittest
from typing import Any
from unittest.mock import mock_open, patch
import sys
sys.path.insert(0, 'path_to_widget/src')


class TestUtils(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_transactions_total(self, mock_file) -> None:
        from src.utils import transactions_total
        result = transactions_total('dummy_path')
        print(result)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='not a json')
    def test_transactions_total_invalid_json(self, mock_file) -> None:
        from src.utils import transactions_total
        result = transactions_total('dummy_path')
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=False)
    def test_transactions_total_file_not_found(self, mock_exists) -> None:
        from src.utils import transactions_total
        result = transactions_total('dummy_path')
        self.assertEqual(result, [])


class TestExternalAPI(unittest.TestCase):
    @patch('src.external_api1.requests.get')
    def test_convert_to_rub(self, mock_get: Any) -> None:
        from src.external_api1 import convert_to_rub
        mock_get.return_value.json.return_value = {'result': 75.0}
        mock_get.return_value.raise_for_status = lambda: None

        amount_in_rub = convert_to_rub(100, 'USD')
        self.assertEqual(amount_in_rub, 75.0)

    def test_convert_invalid_currency(self) -> None:
        from src.external_api1 import convert_to_rub
        with self.assertRaises(ValueError):
            convert_to_rub(100, 'JPY')


if __name__ == '__main__':
    unittest.main()
