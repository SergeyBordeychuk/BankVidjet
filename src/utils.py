import json


def transaction_list(path: str) -> list:
    """Функция возвращает транзакции из файла"""
    try:
        with open(path, encoding="utf-8") as file_in:
            try:
                data = json.load(file_in)
                if not isinstance(data, list):
                    return []
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
    except FileNotFoundError:
        return []
    except OSError:
        return []
    return data
