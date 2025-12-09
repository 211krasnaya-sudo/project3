import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("card_account, expected_card", [
    ("Visa Platinum 7000792244556677", "Visa Platinum 7000 79** **** 6677")])
def test_mask_account_card(card_account, expected_card):
    assert mask_account_card(str(card_account)) == expected_card


@pytest.mark.parametrize("mask_num_card, expected_result", [
    ("Visa Platinum 7000792244556677", "Visa Platinum 7000 79** **** 6677")])
def test_mask_with_error(mask_num_card, expected_result):
    if not str(mask_num_card) != 2:
        with pytest.raises(TypeError):
            raise str(mask_num_card) == expected_result == "Строка должна содержать тип и номер карты"


@pytest.mark.parametrize("card_account_num, expected_num", [
    ("Visa Platinum 7000792244556677", "Visa Platinum 7000 79** **** 6677")])
def test_mask_account_card(card_account_num, expected_num):
    if len(card_account_num) < 8:
        raise str(card_account_num) == expected_num == "Номер счета должен содержать минимум 8 цифр"


@pytest.mark.parametrize("change_data, expected_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(change_data, expected_date):
    assert get_date(str(change_data)) == expected_date


@pytest.mark.parametrize("data_account, expected_data", [
    ("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(data_account, expected_data):
    if len(data_account) != expected_data:
        with pytest.raises(TypeError):
            raise TypeError("Неверно указана дата")
