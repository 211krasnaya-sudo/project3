import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


def test_transaction_descriptions(transactions_currency):
    trans_descrip = transaction_descriptions(transactions_currency)
    assert list(trans_descrip) == ["Перевод", "Перевод с карты"]


@pytest.mark.parametrize("card_start, stop, expected_cards", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (4, 7, ["0000 0000 0000 0004", "0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"])
])
def test_card_number_generator_v2(card_start: int, stop: int, expected_cards: int) -> None:
    result = list(card_number_generator(card_start, stop))
    assert list(result) == expected_cards


@pytest.mark.parametrize("expected", [
    "0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003",
    "0000 0000 0525 2525", "0000 0000 0525 2526", "0000 0000 0525 2527"
])
def test_card_number_generator_v1(expected) -> None:
    x = card_number_generator(1, 3)
    y = card_number_generator(5252525, 5252527)
    assert next(x) == "0000 0000 0000 0001"
    assert next(x) == "0000 0000 0000 0002"
    assert next(x) == "0000 0000 0000 0003"
    assert next(y) == "0000 0000 0525 2525"
    assert next(y) == "0000 0000 0525 2526"
    assert next(y) == "0000 0000 0525 2527"


@pytest.mark.parametrize("card_numbers", [
    "0000234567891234111", "0000 0000 0000 0002", "0000 0000 0000 0003",
    "0000 0000 0000 0004", "0000 0000 0000 0005", "0000 0000 0000 0006"
])
def test_card_number_generator(card_numbers: str) -> None:
    assert len(card_numbers) != 16
    assert card_numbers.replace(" ", "").isdigit()
