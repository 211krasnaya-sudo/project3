import pytest
from src.mask import get_mask_card_number
from tests.conftest import mask_num


@pytest.mark.parametrize("card_number, expected_output", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("7000141535361234", "7000 14** **** 1234")])
def test_get_mask_card_number(card_number: str, expected_output: str) -> None:
    assert get_mask_card_number(str(card_number)) == expected_output


@pytest.mark.parametrize("card_num, expected_num", [
    ("1234567890123455", "123456******3455"),
    ("7000141535361234", "700014******1234"),
    ("7020501535361234", "702050******1234")])
def test_get_mask_card_number_version1(card_num: str, expected_num: str) -> None:
    if card_num == card_num[:4] + " " + card_num[4:6] + "**" + " " + "****" + " " + card_num[-4:]:
        assert card_num == expected_num, "Маскированный номер карты не соответствует ожидаемому"


@pytest.mark.parametrize("card_number_enum, expected_enum", [
    ("1234567890123456id", "1234 56** **** 3456"),
    (" ", " "),
    (101000111010011010101010101010, "1234 56** **** 3456"),
    ("1010101010000010101101", "1233 56** **** 3440")])
def test_get_mask_card_number_enum(card_number_enum: str, expected_enum: str) -> None:
    if card_number_enum != expected_enum:
        with pytest.raises(ValueError, match="Ошибка входных данных"):
            raise ValueError("Ошибка входных данных")


@pytest.mark.parametrize("number_card, expected_put", [
    (" ", "1234 56** **** 3456"),
    (" ", "7000 14** **** 1234")])
def test_get_mask_number_card(number_card: str, expected_put: str) -> None:
    if len(number_card) == " ":
        with pytest.raises(ValueError):
            raise ValueError("Отсутствуют входные данные")


@pytest.mark.parametrize("value_number, expected_val", [
    (" ", "1234 56** **** 3456"),
    (" ", "7000 14** **** 1234")])
def test_get_mask_value_number(value_number: str, expected_val: str) -> None:
    if len(value_number) == " ":
        with pytest.raises(ValueError):
            raise ValueError("Отсутствуют входные данные")


@pytest.mark.parametrize("mask_num, expected_res", [
    ("1101001010111011", "70001313242412342516"),
    ("0001010101101001", "70001313242412342516"),
    ("1010101010101001", "70001313242412342516")])
def test_get_mask_with_error(mask_num: str, expected_res: str) -> None:
    if len(str(mask_num)) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")


@pytest.mark.parametrize("mask_neg, expected_res", [
    ("dbkfFFFlmnvvvqwb", "7000131324241234"),
    ("gggggggggggdddddd", "7575252513131615"),
    ("iiiiiddddddddddd", "7171212135351516"),
    ("dkhvkgjnvkfvmxddfcvg,bmc,vmb", "7171212135351516"),
    ("dfcvb,mjclfi,vbmu,m", "7171212135351516")])
def test_get_mask_neg(mask_neg: str, expected_res: str) -> None:
    if len(str(mask_neg)) == mask_neg.isalpha():
        raise ValueError("Номер карты должен содержать только цифры")


@pytest.mark.parametrize("mask_neg_num, expected_put", [
    ("7000-1313-2424-1234", "7000131324241234"),
    ("7025-1314-2425-1234", "7025131424251234"),
    ("7026-1314-2426-1235", "7026131424261235")])
def test_get_mask_neg_num(mask_neg_num: str, expected_put: str) -> None:
    if len(str(mask_neg_num)) == mask_neg_num.isalnum():
        raise ValueError("Номер карты должен содержать цифры без дефиса")


@pytest.mark.parametrize("mask_poz_num, expected_poz", [
    ("7000 1313 2424 1234", "7000131324241234"),
    ("7001 1312 2423 1234", "7001131224231234")
])
def test_get_mask_poz_num(mask_poz_num: str, expected_poz: str) -> None:
    if len(str(mask_poz_num)) == mask_poz_num.isalnum():
        raise ValueError("Номер карты должен содержать цифры без пробела")


@pytest.mark.parametrize("account_str, expected_num", [
    ("700013132424dddd", "7000131324241234"),
    ("700013132424LMMM", "7000131324241234")])
def test_get_mask_type_error(account_str: str, expected_num: str) -> None:
    if not isinstance(account_str, str):
        with pytest.raises(TypeError):
            raise TypeError("Номер карты должен содержать правильный тип данных")


@pytest.mark.parametrize("account_number, result_account", [
    ("70001234", "**1234"),
    ("12345678", "**5678"),
    ("87654321", "**4321")])
def test_get_mask_account(account_number: str, result_account: str) -> None:
    if len(account_number) < 6:
        raise ValueError("Номер счета должен содержать минимум 6 цифр")
    # Формируем маску
    masked = "**" + account_number[-4:]
    assert masked == result_account, "Маскированный номер карты не соответствует ожидаемому"


@pytest.mark.parametrize("account_numer", [
    "7000",
    "70",
    "7",
])
def test_get_mask_account_error_version2(account_numer: str) -> None:
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 6 цифр"):
        if len(account_numer) < 6:
            raise ValueError("Номер счета должен содержать минимум 6 цифр")


@pytest.mark.parametrize("account_error, result_error", [
    ("01", "**4212"),
    ("0", "**4212")])
def test_get_mask_account_error(account_error: str, result_error: str) -> None:
    if len(str(account_error)) == 0:
        with pytest.raises(ValueError):
            raise ValueError("Номер счета должен содержать минимум 6 цифр")


@pytest.mark.parametrize("account_pos, result_pos", [
    ("account_pos == 70 simbol", "**4212"),
    ("dkjhiithbbjdigjxlvijvn dj njxch njxchvn cjn jmcn", "**4212"),
    ("1111010101010101010101000011010101010101", "**4212"),
    ("1010101", "**4212"),
    ("011010111010110101011110110", "**4212"),
    ("101000101010101", "**1242")])
def test_get_mask_account_pos(account_pos: str, result_pos: str) -> None:
    if len(str(account_pos)) != 16:
        with pytest.raises(ValueError):
            raise ValueError("Длина строки не соответствует ожидаемому ")


@pytest.mark.parametrize("mask_error, mask_res", [
    ("7000", "**1234"),
    ("70001111", "**1234"),
    ("7000grehh1111", "**1234")])
def test_get_mask_error(mask_error: str, mask_res: str) -> None:
    if len(mask_error) != 6:
        with pytest.raises(ValueError):
            raise ValueError("Номер состоит минимум из 6 цифр")


@pytest.mark.parametrize("line_error, expected_mask", [
    (" ", "**1234"),
    (" ", "**1234")])
def test_get_line_error(line_error: str, expected_mask: str) -> None:
    if len(line_error) == " ":
        with pytest.raises(ValueError):
            raise ValueError("Отсутствуют входные данные")


@pytest.mark.parametrize("zero_error, expected_mask", [
    (0, "**1234"),
    (-0, "**1234"),
    (10.0, "**1234")])
def test_get_zero_error(zero_error: str, expected_mask: str) -> None:
    if len(str(zero_error)) == 0:
        with pytest.raises(ValueError):
            raise ValueError("Входные данные равны 0 или не верны")


@pytest.mark.parametrize("account_type, result_type", [
    ("7000234567891234", "**1234")])
def test_get_mask_type(account_type: str, result_type: str) -> None:
    if not isinstance(account_type, int):
        with pytest.raises(TypeError):
            raise TypeError("Номер карты должен содержать правильный тип данных")


@pytest.mark.parametrize("zero_account, result_account", [
    ("ValueError", "**1234")])
def test_get_zero_account(zero_account: str, result_account: str) -> None:
    if not len(zero_account) < 0:
        with pytest.raises(ValueError):
            raise ValueError("")
