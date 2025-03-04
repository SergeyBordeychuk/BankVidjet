import re


def search_operations(list_operations:list, str_search:str) -> list:
    list_dict = []
    for operation in list_operations:
        operation_find = re.findall(str_search, operation, flags=0)
        if operation_find:
            list_dict.append(operation)
    return list_dict
