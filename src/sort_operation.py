def sort_operations(list_operations:list, list_category:list) -> dict:
    result_dict = {}
    for category in list_category:
        count = 0
        for operation in list_operations:
            if category in operation:
                count +=1
        result_dict[category] = count
    return result_dict
