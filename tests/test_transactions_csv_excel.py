from unittest.mock import patch

import pandas as pd

from src.transactions_csv_excel import reading_transaction_csv, reading_transaction_excel


@patch("pandas.read_csv")
def test_reading_transaction_csv(mock_reading_csv):
    test_file_path = 'data/transactions_csv'
    expected_result = [
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
         'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
         'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': ';29740',
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
         'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}
    ]
    # Мокируем pd.read_csv чтобы вернуть DataFrame
    mock_reading_csv.return_value = pd.DataFrame(expected_result)
    result = reading_transaction_csv(test_file_path, delimiter=";")
    assert result == expected_result


def test_reading_transaction_csv_if_file_not_found():
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = reading_transaction_csv('nonexistent.csv')
        assert result == []


@patch("pandas.read_excel")
def test_reading_transaction_excel_v1(mock_reading_excel):
    expected_result = [
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
         'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
         'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': ';29740',
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
         'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}
    ]
    mock_reading_excel.return_value = pd.DataFrame(expected_result)
    result = reading_transaction_excel('dummy.xlsx')
    assert result == expected_result


def test_reading_transaction_excel_if_file_not_found():
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = reading_transaction_excel('nonexistent.xlsx')
        assert result == []
