def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция, которая возвращает новый список словарей. """
    new_list_dict = []

    for stat in list_dict:
        if stat.get("state") == state:
            new_list_dict.append(stat)

    return new_list_dict
