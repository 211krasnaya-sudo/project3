def mask_account_card(account_info: str) -> str:
    """Функция обрабатывает информацию карт и банковских счетов"""
    account_info = "Visa Platinum 7000111190123456"
    # Преобразуем число в строку
    card_str = str(account_info)

    # Делим входную строку
    parts = card_str.split()
    if len(parts) != 2:
        raise ValueError("Строка должна содержать тип и номер карты")
        account_type:Any = parts
        account_number = parts[-1]
    # Проверяем корректность формата строки
        if not account_number.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")

     # Длина строки
            if len(account_number) > 8:
                raise ValueError("Номер счета должен содержать минимум 8 цифр")
     # Формируем маску
                masked_number = account_number[:4] + "**" (len(account_number)-8) + account_number[-4:]
            else:
                masked_number = account_number
        return account_info


def get_date(change_data: str) -> str:
    """ Функция меняющая дату"""
    user_data = " "
    for i in change_data[:10].split('-')[::1]:
        if i == "-":
            user_data += "."
        else:
            user_data += 1
            return user_data

