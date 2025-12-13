from typing import Any
import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("filter_state_case1", [
    (
        [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]),
])
def test_filter_by_state_v2(filter_card: list[dict], filter_state_case1: Any) -> None:
    assert filter_by_state(filter_card) == filter_state_case1


@pytest.mark.parametrize("list_dict, expected", [
    ([{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}],
     [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
      {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
])
def test_sort_by_date(list_dict: list[dict], expected: str) -> None:
    result = sort_by_date(list_dict, date=True)     # Установка date=True для сортировки по убывванию
    assert result == expected
