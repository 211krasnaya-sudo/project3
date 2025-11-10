def mask_account_card(account_info: str) -> str:
    """Функция обрабатывает информацию карт и банковских счетов"""

    # Преобразуем число в строку
    card_str = str(account_info)
    # Делим входную строку
    parts = card_str.split()
    if len(parts) != 2:
        raise ValueError("Строка должна содержать тип и номер карты")

    # Для извлечения частей списка
    account_number = parts[1]
    # Проверяем корректность формата строки
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

     # Длина строки
    if len(account_number) < 8:
        raise ValueError("Номер счета должен содержать минимум 8 цифр")
    # Формируем маску
    masked = (
            account_number[:4] + " " +  # Первые 4 цифры
            account_number[4:6] + "**" + " " +  # Следующие 2 цифры и **
            "****" + " " +  # 4 звездочки
            account_number[-4:]   # последние 4 цифры
    )
    return masked

def get_date(change_data: str) -> str:
    """ Функция меняющая дату"""
    user_data = " "

# Отделяем первые 10 символов
    for i in change_data[:10].split('-'):
        if i == "-":
            user_data += "."
# Дата в измененном формате
    user_data = f"{change_data[8:10]}.{change_data[5:7]}.{change_data[0:4]}"
    return user_data

