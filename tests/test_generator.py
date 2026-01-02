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


def test_transaction_descriptions(list_dict: list[dict]) -> None:
    x = transaction_descriptions([list_dict[0]])
    assert list(x) == ['Перевод', 'Перевод с карты']


@pytest.mark.parametrize("card_start, stop, expected_cards", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (4, 7, ["0000 0000 0000 0004", "0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"])
])
def test_card_number_generator_v2(card_start: int, stop: int, expected_cards: int) -> None:
    result = list(card_number_generator(card_start, stop))
    assert list(result) == expected_cards


@pytest.mark.parametrize("expected", [
    "0000 3232 5454 6565", "0000 0000 0000 1234", "0000 0000 0000 4567",
    "0000 0000 0000 0004", "0000 0000 0000 0005", "0000 0000 0000 0006"
])
def test_card_number_generator_v1(expected: str) -> None:
    generator = card_number_generator(0, 7000000000001234)
    for expected_number in expected:
        assert next(generator) == expected_number


@pytest.mark.parametrize("card_numbers", [
    "0000234567891234111", "0000 0000 0000 0002", "0000 0000 0000 0003",
    "0000 0000 0000 0004", "0000 0000 0000 0005", "0000 0000 0000 0006"
])
def test_card_number_generator(card_numbers: str) -> None:
    assert len(card_numbers) != 16
    assert card_numbers.replace(" ", "").isdigit()
