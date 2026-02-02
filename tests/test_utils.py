import unittest
from unittest.mock import patch
from src.utils import transactions_total


class TestTransactions(unittest.TestCase):

    @patch('src.external_api.convert_to_rub')
    def test_transaction_total_v1(self, mock_convert_to_rub):
        mock_convert_to_rub.return_value = 75.0
        example_transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}}
        result = transactions_total(example_transaction)
        assert result == "USD"
        mock_convert_to_rub.assert_called()


    @patch('src.external_api.convert_to_rub')
    def test_transactions_total_v2(self, mock_convert_to_rub):
        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
        result = transactions_total(transaction)
        self.assertEqual(result, 100.0)
