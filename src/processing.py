from typing import Union


def filter_by_state(list_get: Union[list], state="EXECUTED") -> list:
    """Возвращает словари с ключом state"""
    new_list = []
    for dictionary in list_get:
        for value in dictionary.values():
            if value == state:
                new_list.append(dict)
    return new_list
