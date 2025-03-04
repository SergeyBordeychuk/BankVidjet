from collections import Counter


def sort_operations(list_operations:list, list_category:list) -> dict:
    result_dict = {}
    descriptions = []
    for operation in list_operations:
        if operation != {}:
            descriptions.append(operation['description'])
    counted = Counter(descriptions)
    for key, value in counted.items():
        for category in list_category:
            if key == category:
                result_dict[category] = value
    return result_dict
