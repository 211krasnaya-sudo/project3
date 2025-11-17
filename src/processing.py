def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция, которая возвращает новый список словарей. """
    new_list_dict = []    # Создаем новый список словарей

    for stat in list_dict:
        if stat.get("state") == state:    # Делаем запрос ключ - значение
            new_list_dict.append(stat)    # Добавляем соответствующее ключ-значение

    return new_list_dict


def sort_by_date(list_dict: list[dict], date: bool = True) -> list[dict]:
    """ Функция сортировки списка словарей по дате"""
    sorted_list_dict = sorted(list_dict, key=lambda x: x["date"], reverse=date)
    return sorted_list_dict

