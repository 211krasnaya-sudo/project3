import json
import os
import tempfile
import unittest

from main import transactions_tot


class TestTransactionsTot(unittest.TestCase):

    def _create_temp_file(self, data):
        """Создаём временный файл и возвращаем его путь + cleanup."""
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json', mode='w', encoding='utf-8')
        json.dump(data, temp_file, ensure_ascii=False)
        temp_file.close()
        self.addCleanup(lambda: os.unlink(temp_file.name))
        return temp_file.name

    def test_transactions_tot(self):
        """Проверяем, что функция правильно загружает данные."""
        test_data = [
            {
                "id": "1995784",
                "state": "CANCELED",
                "date": "2023-07-04T16:45:09Z",
                "operationAmount": {
                    "amount": "21185",
                    "currency": {
                        "name": "Dollar",
                        "code": "USD"
                    }
                },
                "from": "Счет 21198763177103220132",
                "to": "Счет 70934017444707070769",
                "description": "Перевод со счета на счет"
            },
            {
                "id": "4234093",
                "state": "EXECUTED",
                "date": "2021-07-08T07:31:21Z",
                "operationAmount": {
                    "amount": "23182",
                    "currency": {
                        "name": "Ruble",
                        "code": "RUB"
                    }
                },
                "from": "Visa 0773092093872450",
                "to": "Discover 8602781449570491",
                "description": "Перевод с карты на карту"
            }
        ]

        file_path = self._create_temp_file(test_data)
        result = transactions_tot(file_path)

        expected = [
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
                'id': '4234093',
                'state': 'EXECUTED',
                'date': '2021-07-08T07:31:21Z',
                'amount': '23182',
                'currency_name': 'Ruble',
                'currency_code': 'RUB',
                'from': 'Visa 0773092093872450',
                'to': 'Discover 8602781449570491',
                'description': 'Перевод с карты на карту'
            }
        ]

        self.assertEqual(result, expected)

    def test_empty_file(self):
        """Тестируем поведение на пустом JSON-файле."""
        file_path = self._create_temp_file([])
        result = transactions_tot(file_path)
        self.assertEqual(result, [])

    def test_missing_fields(self):
        """Тестируем обработку операций с отсутствующими полями."""
        test_data = [
            {
                "id": "3",
                "state": "EXECUTED",
                "date": "2021-01-03T00:00:00Z",
                "description": "Тест без суммы"
            }
        ]
        file_path = self._create_temp_file(test_data)

        result = transactions_tot(file_path)
        expected = [
            {
                'id': '3',
                'state': 'EXECUTED',
                'date': '2021-01-03T00:00:00Z',
                'amount': '',
                'currency_name': '',
                'currency_code': '',
                'from': '',
                'to': '',
                'description': 'Тест без суммы'
            }
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
