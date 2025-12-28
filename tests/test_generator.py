import pytest
from src.generators import filter_by_currency, card_number_generator, transaction_descriptions


@pytest.mark.parametrize("transactions, currency", [
    ([{
        "id": 939719570,
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        }
    }], "USD")
])
def test_filter_by_currency(transactions: list[dict], currency: str) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result


def test_transaction_descriptions(list_dict) -> None:
    x = transaction_descriptions(list_dict[0])
    assert next(x) == 'Перевод'
    assert next(x) == 'Перевод с карты'


@pytest.mark.parametrize("card_start, stop, expected_cards", [
    (1, 3, ["7000 0000 0000 0001", "7000 0000 0000 0002", "7000 0000 0000 0003"]),
    (4, 7, ["7000 0000 0000 0004", "7000 0000 0000 0005", "7000 0000 0000 0006", "7000 0000 0000 0007"])
])
def test_card_number_generator(card_start, stop, expected_cards) -> None:
    result = list(card_number_generator(card_start, stop))
    assert next(result) == expected_cards
