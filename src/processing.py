from typing import Union


def filter_by_state(list_get: Union[list], state: Union[str] = "EXECUTED") -> list:
    """Возвращает словари с ключом state"""
    new_list = []
    for dictionary in list_get:
        for value in dictionary.values():
            if value == state:
                new_list.append(dict)
    return new_list


def sort_by_date(list_get: Union[list], revers: Union[bool] = True) -> list:
    """Возвращаеь словари отсортированные по датам"""
    new_list = []
    dates = []
    for dictionary in list_get:
        dates.append(dictionary.get("date"))
        dates = sorted(dates, reverse=revers)
    for date in dates:
        for diction in list_get:
            if date == diction.get("date"):
                new_list.append(diction)
    return new_list
