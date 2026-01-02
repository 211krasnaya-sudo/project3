def get_mask_card_number(card_number: str) -> str:
    """ Маскирует номер карты, оставляя первые 6 и последние 4 цифры видимыми."""
    # Преобразуем число в строку
    card_str = str(card_number)
    # Проверяем корректность длины номера карты
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    # Фотмируем маску
    masked = (card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:])
    return masked


def get_mask_account(account_number: int) -> str:
    """ Маскирует номер счёта по шаблону **xxxx"""
    # Преобразуем число в строку
    account_str = str(account_number)
    # Проверяем минимальную длину номера счета
    if len(account_str) < 20:
        raise ValueError("Номер счета должен содержать минимум 20 цифр")
    # Формируем маску
    masked = "**" + account_str[-4:]
    return masked
