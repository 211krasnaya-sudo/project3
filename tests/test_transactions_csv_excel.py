import pandas as pd
from unittest.mock import patch

from src.transactions_csv_excel import reading_transaction_csv, reading_transaction_excel


@patch("pandas.read_csv")
def test_reading_transaction_csv(mock_reading_csv, mock_df=None):
    # Мокируем pd.read_csv чтобы вернуть DataFrame
    mock_reading_csv.return_value = pd.DataFrame({'date': ['2025-04-02'], 'amount': [200], 'description': ['Test']})
    patch('transactions_reader.pd.read_csv', return_value=mock_df)
    result = reading_transaction_csv('dummy.csv')
    result = reading_transaction_csv('test_csv')
    assert result == [{'date': '2025-04-02', 'amount': 200, 'description': 'Test'}]


def test_reading_transaction_csv_if_file_not_found():
    result = reading_transaction_csv('nonexistent.csv')
    assert result == []

def test_reading_transaction_excel_v1(mock_reading_csv, mock_df=None):
    mock_reading_csv.return_value = pd.DataFrame({'date': ['2025-04-02'], 'amount': [200], 'description': ['Test']})
    patch('transactions_reader.pd.read_csv', return_value=mock_df)
    result = reading_transaction_excel('dummy.csv')
    assert result == [{'date': '2025-04-02', 'amount': 200, 'description': 'Test'}]

def test_reading_transaction_excel_if_file_not_found():
    result = reading_transaction_excel('nonexistent.csv')
    assert result == []
