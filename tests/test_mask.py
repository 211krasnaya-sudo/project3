import pytest
from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected_output", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("7000141535361234", "7000 14** **** 1234")])
def test_get_mask_card_number(card_number, expected_output):
    assert get_mask_card_number(str(card_number)) == expected_output


@pytest.mark.parametrize("number_card, expected_put", [
    (" ", "1234 56** **** 3456"),
    (" ", "7000 14** **** 1234")])
def test_get_mask_number_card(number_card, expected_put):
    if len(number_card) == " ":
        with pytest.raises(ValueError):
            raise ValueError("Отсутствуют входные данные")


@pytest.mark.parametrize("value_number, expected_val", [
    (" ", "1234 56** **** 3456"),
    (" ", "7000 14** **** 1234")])
def test_get_mask_value_number(value_number, expected_val):
    if len(value_number) == " ":
        with pytest.raises(ValueError):
            raise ValueError("Отсутствуют входные данные")


@pytest.mark.parametrize("mask_num, expected_res", [
    ("7000131324241234", "7000131324241234")])
def test_get_mask_with_error(mask_num, expected_res):
    if len(str(mask_num)) != 16:
        raise str(mask_num) == expected_res == "Номер карты должен содержать 16 цифр"


@pytest.mark.parametrize("account_str, expected_num", [
    ("7000131324241234", "7000131324241234")])
def test_get_mask_type_error(account_str, expected_num):
    if not isinstance(account_str, str):
        with pytest.raises(TypeError):
            raise TypeError("Номер карты должен содержать правильный тип данных")


@pytest.mark.parametrize("account_number, result_account", [
    ("7000234567891234", "**1234")])
def test_get_mask_account(account_number, result_account):
    if not len(account_number) < 6:
        with pytest.raises(ValueError):
            raise ValueError("Маскировка номера минимум 6 цифр")


@pytest.mark.parametrize("account_error, result_error", [
    ("7500265200004212", "**4212")])
def test_get_mask_account_error(account_error, result_error):
    if len(str(account_error)) < 6:
        with pytest.raises(ValueError):
            raise str(account_error) == result_error == "Номер счета должен содержать минимум 6 цифр"


@pytest.mark.parametrize("mask_error, mask_res", [
    ("7000", "**1234")])
def test_get_mask_error(mask_error, mask_res):
    if len(mask_error) != 6:
        with pytest.raises(ValueError):
            raise ValueError("Номер состоит минимум из 6 цифр")

@pytest.mark.parametrize("line_error, expected_mask", [
    (" ", "**1234")])
def test_get_line_error(line_error, expected_mask):
    if len(line_error) == " ":
        with pytest.raises(ValueError):
            raise ValueError("Отсутствуют входные данные")

@pytest.mark.parametrize("zero_error, expected_mask", [
    (0, "**1234")])
def test_get_zero_error(zero_error, expected_mask):
    if len(str(zero_error)) == 0:
        with pytest.raises(ValueError):
            raise ValueError("Входные данные равны 0")

@pytest.mark.parametrize("account_type, result_type", [
    ("7000234567891234", "**1234")])
def test_get_mask_type(account_type, result_type):
    if not isinstance(account_type, int):
        with pytest.raises(TypeError):
            raise TypeError("Номер карты должен содержать правильный тип данных")

@pytest.mark.parametrize("zero_account, result_account", [
    ("ValueError", "**1234")])
def test_get_zero_account(zero_account, result_account):
    if not len(zero_account) < 0:
        with pytest.raises(ValueError):
            raise ValueError("")
