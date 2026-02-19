import unittest
from unittest.mock import patch
from typing import Any


class TestExternalAPI(unittest.TestCase):
    @patch('src.external_api1.requests.get')
    def test_convert_to_rub_v1(self, mock_get: Any) -> None:

        from src.external_api1 import convert_to_rub
        mock_get.return_value.json.return_value = {'result': 75.0}
        mock_get.return_value.raise_for_status = lambda: None

        amount_in_rub = convert_to_rub(str(100), 'USD')
        self.assertEqual(amount_in_rub, 75.0)

    def test_convert_invalid_currency(self) -> None:
        from src.utils import convert_to_rub
        with self.assertRaises(ValueError):
            convert_to_rub(str(100), 'JPY')


if __name__ == '__main__':
    unittest.main()