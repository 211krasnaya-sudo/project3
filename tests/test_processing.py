from typing import Any
import pytest
from src.processing import filter_by_state, sort_by_date
from tests.conftest import filter_card


@pytest.mark.parametrize("filter_state_case1, expected_filter", [
    ("EXECUTED",
     [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]),
])
def filter_by_state_v2(filter_card: list[dict], filter_state_case1: Any, expected_filter: str) -> None:
    assert filter_by_state(filter_state_case1) == expected_filter


@pytest.mark.parametrize("filter_state_case2, expected_filter_neg", [
    ("EXECUTED",
     [{"id": 41428829, "state": "EXEC-UTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXEC-UTED", "date": "2018-06-30T02:08:58.425572"}])
])
def test_filter_by_state_neg(filter_by_state_neg: str, filter_state_case2: str, expected_filter_neg: str) -> None:
    if len(str(filter_by_state_neg)) == filter_state_case2.isalnum():
        raise ValueError("Номер карты должен содержать цифры без дефиса")


@pytest.mark.parametrize("filter_card, expected_card", [
    ("CANCELED",
     [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
      {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]),
])
def test_filter_card(filter_card: str, expected_card: str) -> None:
    if not enumerate("state") != expected_card:
        with pytest.raises(AttributeError):
            raise AttributeError("Строка должна содержать правильный атрибут")


@pytest.mark.parametrize("list_dict, expected", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_by_date(list_dict: list[dict], expected: str) -> None:
    result = sort_by_date(list_dict, date=True)     # Установка date=True для сортировки по убывванию
    assert result == expected


@pytest.mark.parametrize("list_dictor, expected_error", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_by_error(list_dictor: list[dict], expected_error: str) -> None:
    result = sort_by_date(list_dictor, date=False)     # Установка date=False
    assert result != expected_error


@pytest.mark.parametrize("list_error, expected_mask_case1", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_mask_error_case1(list_error: str, expected_mask_case1: str) -> None:
    if not enumerate(list_error) != expected_mask_case1:
        with pytest.raises(ValueError):
            raise ValueError("Ошибка входных данных")


@pytest.mark.parametrize("sort_mask_error, expected_mask_case2", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_mask_error_case2(sort_mask_error: Any, expected_mask_case2: Any) -> None:
    if not enumerate(sort_mask_error) != expected_mask_case2:
        with pytest.raises(ValueError, match="Ошибка входных данных"):
            raise ValueError("Ошибка входных данных")
