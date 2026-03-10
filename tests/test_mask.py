import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected_output", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("7000141535361234", "7000 14** **** 1234")])
def test_get_mask_card_number(card_number: str, expected_output: str) -> None:
    assert get_mask_card_number(str(card_number)) == expected_output


@pytest.mark.parametrize("value_number, expected_val", [
    (" ", "1234 56** **** 3456"),
    (" ", "7000 14** **** 1234")])
def test_get_mask_value_number(value_number: str, expected_val: str) -> None:
    if len(value_number) == " ":
        with pytest.raises(ValueError):
            get_mask_card_number(value_number)


@pytest.mark.parametrize("mask_num, expected_res", [
    ("11010010101110", "70001313242412342516"),
    ("000101101001", "70001313242412342516"),
    ("1010101001", "70001313242412342516")])
def test_get_mask_with_error(mask_num: str, expected_res: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(mask_num)


@pytest.mark.parametrize("mask_neg, expected_res", [
    ("01011", "7000131324241234"),
    ("52551215", "7575252513131615"),
    ("0101101101", "7171212135351516")])
def test_get_mask_account(mask_neg: int, expected_res: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(mask_neg)


@pytest.mark.parametrize("account_type, result_type", [
    ("70002345678912341110", "**1110")])
def test_get_mask_type(account_type: int, result_type: str) -> None:
    assert get_mask_account(account_type) == result_type
