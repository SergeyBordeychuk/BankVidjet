from typing import Union


def mask_account_card(card: Union[str]) -> str:
    """Маскировка счёта или карты"""
    if "Счет" in card:
        return f"Счет **{card[-4:]}"
    else:
        return f"{card[:-17]} {card[-17:-12]} {card[-12:-10]}** **** {card[-4:]}"


def get_date(date: Union[str]) -> str:
    """Получение даты в формате xx.xx.xxxx"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
