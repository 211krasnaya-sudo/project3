import unittest
from typing import Any, Dict, List

from src.transactions_post import process_bank_operations, process_bank_search


class TestBankOperations(unittest.TestCase):
    def setUp(self):
        """Метод, который выполняется перед каждым тестом, для подготовки общих данных."""
        self.account: List[Dict[str, Any]] = [
            {
                'id': '4234093',
                'state': 'EXECUTED',
                'date': '2021-07-08T07:31:21Z',
                'amount': '23182',
                'currency_name': 'Ruble',
                'currency_code': 'RUB',
                'from': 'Visa 0773092093872450',
                'to': 'Discover 8602781449570491',
                'description': 'Перевод с карты на карту'
            },
            {
                'id': '1995784',
                'state': 'CANCELED',
                'date': '2023-07-04T16:45:09Z',
                'amount': '21185',
                'currency_name': 'Dollar',
                'currency_code': 'USD',
                'from': 'Счет 21198763177103220132',
                'to': 'Счет 70934017444707070769',
                'description': 'Перевод со счета на счет'
            },
            {
                'id': '4813301',
                'state': 'EXECUTED',
                'date': '2021-11-02T13:32:15Z',
                'amount': '15080',
                'currency_name': 'Euro',
                'currency_code': 'EUR',
                'from': 'Счет 65547878890984510340',
                'to': 'Счет 91457207307678002163',
                'description': 'Перевод со счета на счет'
            },
            {
                'id': '3463793',
                'state': 'PENDING',
                'date': '2020-02-25T07:24:59Z',
                'amount': '17655',
                'currency_name': 'Ruble',
                'currency_code': 'RUB',
                'from': 'Mastercard 4597611385572324',
                'to': 'Visa 0264849140954307',
                'description': 'Перевод с карты на карту'
            }
        ]
    # def setUp(self):
        # self.wasSetUp = 1
        # self.setUp()
        # method = getattr(self, str(self.transactions))
        # method()

    def test_process_bank_search(self):
        """Тестирует функцию поиска по описанию транзакции."""
        search_term = "перевод"
        # Все 4 транзакции содержат "Перевод" — значит, результат должен быть из 4
        expected_result = self.account  # все транзакции подходят
        result = process_bank_search(self.account, search_term)
        self.assertEqual(len(result), 4)
        self.assertEqual(result, expected_result)

    def test_process_bank_operations(self):
        """Тестирует функцию подсчета операций по категориям."""
        categories = ['ожидание', 'отмена', 'перевод']
        expected_result = {
            'ожидание': 0,   # PENDING
            'отмена': 0,     # CANCELED
            'перевод': 4     # все 4 транзакции — "перевод"
        }
        result = process_bank_operations(self.account, categories)
        self.assertEqual(result, expected_result)

    def test_empty_search(self):
        """Тестирует поиск, когда не найдено никаких совпадений."""
        search_term = "некорректный запрос"
        expected_result = []
        result = process_bank_search(self.account, search_term)
        self.assertEqual(result, expected_result)

    def test_empty_transactions(self):
        """Тестирует функции на пустом списке транзакций."""
        empty_transactions = []
        categories = ['перевод', 'отмена', 'ожидание']
        expected_result = {category: 0 for category in categories}

        result_search = process_bank_search(empty_transactions, "перевод")
        result_operations = process_bank_operations(empty_transactions, categories)

        self.assertEqual(result_search, [])
        self.assertEqual(result_operations, expected_result)


if __name__ == '__main__':
    unittest.main()
