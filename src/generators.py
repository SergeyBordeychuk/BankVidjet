def filter_by_currency(transitions: list, currency: str):
    '''Фильтрация по валюте'''
    for transition in transitions:
        if ((transition.get("operationAmount")).get("currency")).get("code") == currency:
            yield transition


def transaction_descriptions(transitions: list):
    '''Описания операций'''
    for transition in transitions:
        yield transition.get("description")


def card_number_generator(first_number: int, last_number: int):
    '''Генератор номеров карт'''
    for number in range(first_number, last_number + 1):
        card_number = "0" * (16 - len(str(number))) + str(number)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:17]}"
