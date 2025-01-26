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
    sorted_list = sorted(catalogue, key=lambda x: x['date'], reverse=revers)
    return sorted_list
