from typing import Union


def get_mask_card_number(card: Union[int, str]) -> str:
    """Создаём маску карты"""
    card = str(card)
    card_mask = card[:6] + "******" + card[12:]
    return card_mask[:4] + " " + card_mask[4:8] + " " + card_mask[8:12] + " " + card_mask[12:]


def get_mask_account(account: Union[int, str]) -> str:
    """Создаём маску счёта"""
    account = str(account)
    account_mask = "**" + account[-4:]
    return account_mask
