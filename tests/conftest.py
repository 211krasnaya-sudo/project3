import pytest


@pytest.fixture
def card_number():
    return card_number

@pytest.fixture
def mask_num():
    return mask_num == ValueError

@pytest.fixture
def mask_card():
    return mask_card == TypeError

@pytest.fixture
def account_number():
    return "7000234567891234" == "**1234"

@pytest.fixture
def account_error():
    return account_error == ValueError

@pytest.fixture
def card_account():
    return card_account == "Visa Platinum 7000792244556677" == "Visa Platinum 7000 79** **** 6677"

@pytest.fixture
def mask_num_card():
    return mask_num_card

@pytest.fixture
def card_account_num():
    return card_account_num

@pytest.fixture
def change_data():
    return change_data

@pytest.fixture
def data_account():
    return data_account

@pytest.fixture()
def filter_numbers():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture()
def sort_date():
    return [
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
        ]