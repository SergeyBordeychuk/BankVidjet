def filter_by_state(catalogue: list, state: str = "EXECUTED") -> list:
    """Возвращает словари с ключом state"""
    sorted_list = []
    for dictionary in catalogue:
        if dictionary.get("state") == state:
            sorted_list.append(dictionary)
    return sorted_list


def sort_by_date(catalogue: list, revers: bool = True) -> list:
    """Возвращаеь словари отсортированные по датам"""
    sorted_list = sorted(catalogue, key=lambda x: x["date"], reverse=revers)
    return sorted_list
