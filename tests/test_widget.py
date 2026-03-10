import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("card_account, expected_output", [
    ("VisaPlatinum7000792244556677", "Visa Platinum 7000 79** **** 6677"),
    ("VisaPlatinum7555792244556677", "Visa Platinum 7555 79** **** 6677")])
def test_mask_account_card(card_account: str, expected_output: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(card_account)


@pytest.mark.parametrize("mask_num_card, expected_result", [
    ("Visa Platinum hhfh244556677", "Visa Platinum 7000 79** **** 6677"),
    ("Visa Platinum 7555hbjnv4556677", "Visa Platinum 7555 79** **** 6677")])
def test_mask_with_error(mask_num_card: str, expected_result: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(mask_num_card)


@pytest.mark.parametrize("card_account_num1, expected_num", [
    ("Visa Platinum 700079244556677", "Visa Platinum 7000 79** **** 6677"),
    ("Visa Platinum 700079224458888", "Visa Platinum 7000 79** **** 8888"),
    ("Visa Platinum 70007922443333", "Visa Platinum 7000 79** **** 3333")])
def test_mask_account_card_version2(card_account_num1: str, expected_num: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(card_account_num1)


@pytest.mark.parametrize("card_account_num, expected_num", [
    ("Visa Platinum 7000792444556677", "Visa Platinum 7000 79** **** 6677"),
    ("Visa Platinum 7000794224458888", "Visa Platinum 7000 79** **** 8888"),
    ("Visa Platinum 7000792552443333", "Visa Platinum 7000 79** **** 3333")])
def test_mask_account_card_version1(card_account_num: str, expected_num: str) -> None:
    assert mask_account_card(card_account_num) == expected_num


@pytest.mark.parametrize("change_data, expected_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-02-11T02:26:18.671407", "11.02.2025")])
def test_get_date(change_data: str, expected_date: str) -> None:
    assert get_date(change_data) == expected_date
