from typing import Union


def filter_by_state(catalogue: Union[list], state: Union[str] = "EXECUTED") -> list:
    """Возвращает словари с ключом state"""
    sorted_list = []
    for dictionary in catalogue:
        for value in dictionary.values():
            if value == state:
                sorted_list.append(dictionary)
    return sorted_list


def sort_by_date(catalogue: Union[list], revers: Union[bool] = True) -> list:
    """Возвращаеь словари отсортированные по датам"""
    new_list = []
    dates = []
    for dictionary in catalogue:
        dates.append(dictionary.get("date"))
        dates = sorted(dates, reverse=revers)
    for date in dates:
        for diction in catalogue:
            if date == diction.get("date"):
                new_list.append(diction)
    return new_list
