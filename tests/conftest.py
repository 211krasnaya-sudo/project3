import pytest


@pytest.fixture
def card_number() -> str:
    number = "1234567890123456"
    return number


@pytest.fixture
def value_number() -> str:
    value_number = " "
    return value_number


@pytest.fixture
def mask_num() -> str:
    mask_num = "1101001010111011"
    return mask_num


@pytest.fixture
def mask_neg() -> str:
    mask_neg = "dbkfFFFlmnvvvqwb"
    return mask_neg


@pytest.fixture
def account_type() -> str:
    account_type = "7000234567891234"
    return account_type


@pytest.fixture
def card_account() -> str:
    card_account = "Visa Platinum 7000792244556677"
    return card_account


@pytest.fixture
def mask_num_card() -> str:
    mask_num_card = "Visa Platinum 7000792244556677"
    return mask_num_card


@pytest.fixture
def card_account_num() -> str:
    card_account_num = "Visa Platinum 7000792244556677"
    return card_account_num


@pytest.fixture
def card_account_num1() -> str:
    card_account_num1 = "Visa Platinum 7000792244556677"
    return card_account_num1


@pytest.fixture
def change_data() -> str:
    change_data = "2024-03-11T02:26:18.671407"
    return change_data


@pytest.fixture
def filter_card() -> list[dict[str, object]]:
    filter_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]
    return filter_data


@pytest.fixture
def transactions_currency() -> list[dict]:
    return [
         {'id': 4142882, 'description': 'Перевод', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 59422672, 'description': 'Перевод с карты', 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]



@pytest.fixture
def filter_gen() -> list[dict[str, object]]:
    filter_gen = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]
    return filter_gen


@pytest.fixture
def card_start() -> str:
    card_start = "7000 2345 6789 1234 "
    return card_start


@pytest.fixture
def card_numbers() -> str:
    card_numbers = "7000000000000002"
    return card_numbers
