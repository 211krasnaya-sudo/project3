import pytest


@pytest.fixture
def card_number() -> str:
    number = "1234567890123456"
    return number

@pytest.fixture
def card_num() -> str:
    num = "1234567890123455"
    return num

@pytest.fixture
def card_number_enum() -> str:
    number_enum = "1234567890123456id"
    return number_enum

@pytest.fixture
def number_card() -> str:
    card = " "
    return card

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
def mask_neg_num() -> str:
    mask_neg_num = "7000-1313-2424-1234"
    return mask_neg_num

@pytest.fixture
def mask_poz_num() -> str:
    mask_poz_num = "7000 1313 2424 1234"
    return mask_poz_num

@pytest.fixture
def account_str() -> str:
    account_str = "700013132424dddd"
    return account_str

@pytest.fixture
def account_number() -> str:
    account_number = "70001234"
    return account_number

@pytest.fixture
def account_numer() -> str:
    account_numer = "7000"
    return account_numer

@pytest.fixture
def account_error() -> str:
    account_error = "01"
    return account_error

@pytest.fixture
def account_pos() -> str:
    account_pos = "1111010101010101010101000011010101010101"
    return account_pos

@pytest.fixture
def mask_error() -> str:
    mask_error = "70001111"
    return mask_error

@pytest.fixture
def line_error() -> str:
    line_error = " "
    return line_error

@pytest.fixture
def zero_error() -> int:
    zero_error = -0
    return zero_error

@pytest.fixture
def zero_account() -> str:
    zero_account = "ValueError"
    return zero_account

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
def change_data() -> str:
    change_data = "2024-03-11T02:26:18.671407"
    return change_data

@pytest.fixture
def data_account() -> str:
    data_account = "2024-05-11T02:26:18.671407"
    return data_account

@pytest.fixture
def filter_numbers() -> list[tuple[str, list[dict]]]:
    filter_numbers = [
    ("EXECUTED",
     [{"id": 41428829, "state": "EXEC-UTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXEC-UTED", "date": "2018-06-30T02:08:58.425572"}])]
    return filter_numbers

@pytest.fixture
def filter_by_state_neg() -> list[tuple[str, list[dict]]]:
    filter_by_state_neg = [
    ("EXECUTED",
     [{"id": 41428829, "state": "EXEC-UTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXEC-UTED", "date": "2018-06-30T02:08:58.425572"}])]
    return filter_by_state_neg

@pytest.fixture
def filter_card() -> list[tuple[str, list[dict]]]:
    filter_card = [
    ("CANCELED",
     [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
      {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}])]
    return filter_card

@pytest.fixture
def list_dict() -> list[list[dict[str, object]]]:
    list_dict = [
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
        ]
    return list_dict

@pytest.fixture
def list_dictor() -> list[list[dict[str, object]]]:
    list_dictor = [
        [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
         {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
         {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
         {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]
        ]
    return list_dictor

@pytest.fixture
def list_error() -> list[list[dict[str, object]]]:
    list_error = [
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
        ]
    return list_error

@pytest.fixture
def sort_mask_error() -> list[tuple[list[dict[str, object]], list[dict[str, object]]]]:
    sort_mask_error = [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}])]
    return sort_mask_error
