import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("filter_state, expected_filter", [
    ("EXECUTED",
     [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]),
])
def test_filter_by_state(filter_numbers, filter_state, expected_filter):
    assert filter_by_state(filter_numbers, filter_state) == expected_filter


@pytest.mark.parametrize("filter_card, expected_card", [
    ("CANCELED",
     [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
      {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]),
])
def test_filter_card(filter_card, expected_card):
    if  not enumerate("state") != expected_card:
        with pytest.raises(AttributeError):
            raise str(filter_card) == expected_card == "Строка должна содержать правильный атрибут"


@pytest.mark.parametrize("list_dict, expected", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_by_date(list_dict, expected):
    result = sort_by_date(list_dict, date = True)     # Установка date=True для сортировки по убывванию
    assert result == expected

@pytest.mark.parametrize("list_dictor, expected_error", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_by_error(list_dictor, expected_error):
    result = sort_by_date(list_dictor, date = False)     # Установка date=False
    assert result != expected_error

@pytest.mark.parametrize("list_error, expected_mask", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_mask_error(list_error, expected_mask):
    result = sort_by_date(list_error, date = True) == expected_mask     # Установка date=True для сортировки по убывванию
    if not enumerate(list_error) != expected_mask:
        with pytest.raises(ValueError):
            raise str(list_error) == expected_mask == "Ошибка входных данных"

