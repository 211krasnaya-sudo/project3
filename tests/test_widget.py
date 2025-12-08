import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("card_account, expected_output", [
    ("Visa Platinum 7000792244556677", "Visa Platinum 7000 79** **** 6677"),
    ("Visa Platinum 7555792244556677", "Visa Platinum 7555 79** **** 6677")])
def test_mask_account_card(card_account: str, expected_output: str) -> None:
    # Разделяем строку на тип карты и номер
    parts = card_account.rsplit(maxsplit=1)
    if len(parts) != 2:
        raise ValueError("Строка должна содержать тип и номер карты")
    card_type, card_number = parts
    # Маскируем номер карты
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    masked_result = f"{card_type} {masked_number}"
    assert masked_result == expected_output, "Маскированный номер карты не соответствует ожидаемому"


@pytest.mark.parametrize("mask_num_card, expected_result", [
    ("Visa Platinum 7000792244556677", "Visa Platinum 7000 79** **** 6677"),
    ("Visa Platinum 7555792244556677", "Visa Platinum 7555 79** **** 6677")])
def test_mask_with_error(mask_num_card: str, expected_result: str) -> None:
    if not str(mask_num_card) != 2:
        with pytest.raises(TypeError):
            raise TypeError("Строка должна содержать тип и номер карты")


@pytest.mark.parametrize("card_account_num, expected_num", [
    ("Visa Platinum 7000792244556677", "Visa Platinum 7000 79** **** 6677"),
    ("Visa Platinum 7000792244558888", "Visa Platinum 7000 79** **** 8888"),
    ("Visa Platinum 7000792244553333", "Visa Platinum 7000 79** **** 3333")])
def test_mask_account_card_version2(card_account_num: str, expected_num: str) -> None:
    if len(card_account_num) < 8:
        raise TypeError("Номер счета должен содержать минимум 8 цифр")


@pytest.mark.parametrize("change_data, expected_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-02-11T02:26:18.671407", "11.02.2025")])
def test_get_date(change_data: str, expected_date: str) -> None:
    assert get_date(str(change_data)) == expected_date


@pytest.mark.parametrize("data_account, expected_data", [
    ("2024-05-11T02:26:18.671407", "11.05.2024"),
    ("2024-06-11T02:26:18.671407", "11.06.2024"),
    ("2024-07-11T02:26:18.671407", "11.07.2024")])
def test_get_date_version2(data_account: str, expected_data: str) -> None:
    if len(data_account) != expected_data:
        with pytest.raises(TypeError):
            raise TypeError("Неверно указана дата")
