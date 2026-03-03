from unittest.mock import patch

import pandas as pd

from src.transactions_csv_excel import reading_transaction_csv, reading_transaction_excel


@patch("pandas.read_csv")
def test_reading_transaction_csv(mock_reading_csv):
    # Мокируем pd.read_csv чтобы вернуть DataFrame
    mock_reading_csv.return_value = pd.DataFrame({'date': ['2025-04-02'], 'amount': [200], 'description': ['Test']})
    result = reading_transaction_csv('test_csv')
    assert result == [{'date': '2025-04-02', 'amount': 200, 'description': 'Test'}]


def test_reading_transaction_csv_if_file_not_found():
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = reading_transaction_csv('nonexistent.csv')
        assert result == []


@patch("pandas.read_excel")
def test_reading_transaction_excel_v1(mock_reading_excel):
    mock_reading_excel.return_value = pd.DataFrame({'date': ['2025-04-02'], 'amount': [200], 'description': ['Test']})
    result = reading_transaction_excel('dummy.xlsx')
    assert result == [{'date': '2025-04-02', 'amount': 200, 'description': 'Test'}]


def test_reading_transaction_excel_if_file_not_found():
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = reading_transaction_excel('nonexistent.xlsx')
        assert result == []
