import unittest
from unittest.mock import patch, MagicMock
from mypy.dmypy.client import request
from src.external_api import convert_to_rub


class TestExternalAPI(unittest.TestCase):
    @patch('requests.get')
    def test_convert_to_rub_v1(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.return_value.json.return_value = {"result": 75.00}    #Пример ответа
        mock_get.return_value = mock_response
        result = convert_to_rub(1.0, "USD")
        self.assertEqual(result, 1.0)
        mock_get.assert_called_once()


    @patch('requests.get')
    def test_convert_to_rub_v2(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Внутренняя ошибка сервера"
        mock_get.return_value = mock_response
        result = convert_to_rub(1.0, "EUR")
        self.assertEqual(result, 0.0)
        #self.assertRaises