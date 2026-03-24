import unittest
import json
import tempfile
from main import transactions_tot

class TestTransactionsTot(unittest.TestCase):
    def setUp(self):
        # Создаем временный JSON файл с тестовыми данными
        self.test_data = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2021-01-01T00:00:00Z",
                "operationAmount": {
                    "amount": "1000",
                    "currency": {
                        "name": "Ruble",
                        "code": "RUB"
                    }
                },
                "from": "Счет 1234",
                "to": "Счет 5678",
                "description": "Перевод"
            },
            {
                "id": "2",
                "state": "CANCELED",
                "date": "2021-01-02T00:00:00Z",
                "operationAmount": {
                    "amount": "2000",
                    "currency": {
                        "name": "Dollar",
                        "code": "USD"
                    }
                },
                "from": "Счет 8765",
                "to": "Счет 4321",
                "description": "Отмена перевода"
            }
        ]
        # Создаем временный файл
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        with open(self.temp_file.name, 'w', encoding='utf-8') as f:
            json.dump(self.test_data, f)

    def tearDown(self):
        # Удаляем временный файл
        import os
        os.remove(self.temp_file.name)

    def test_transactions_tot(self):
        # Проверяем, что функция правильно загружает и преобразует данные
        expected_output = [
            {
                'id': '1',
                'state': 'EXECUTED',
                'date': '2021-01-01T00:00:00Z',
                'amount': '1000',
                'currency_name': 'Ruble',
                'currency_code': 'RUB',
                'from': 'Счет 1234',
                'to': 'Счет 5678',
                'description': 'Перевод'
            },
            {
                'id': '2',
                'state': 'CANCELED',
                'date': '2021-01-02T00:00:00Z',
                'amount': '2000',
                'currency_name': 'Dollar',
                'currency_code': 'USD',
                'from': 'Счет 8765',
                'to': 'Счет 4321',
                'description': 'Отмена перевода'
            }
        ]
        result = transactions_tot(self.temp_file.name)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()