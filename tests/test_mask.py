import pytest

from src.mask import get_mask_card_number, get_mask_account
from tests.conftest import card_number, account_number


@pytest.mark.parametrize("card_number, expected_output", [
    ("1234567890123456", "7000 1456 79** 1234"),
    ("1234567890123456", "7000 14** **** 1234")
])
def test_get_mask_card_number(card_number, expected_output):
    assert get_mask_card_number(card_number) == expected_output
    assert get_mask_card_number(card_number) == "Номер карты должен содержать 16 цифр"


@pytest.mark.parametrize("account_number, expected_number", [
    ("11234567890123456","**4212"),
    ("7000 2345 6789 1234","**1556")
])
def test_get_mask_account(account_number, expected_number):
    assert get_mask_account(int(account_number)) == expected_number