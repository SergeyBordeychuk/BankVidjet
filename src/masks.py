import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("C:/Users/1/PycharmProjects/BankVidjet/logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card: Union[int, str]) -> str:
    """Создаём маску карты"""
    logger.info(f"Начало маскировки номера карты: {card}")
    if card[0].isalpha() == 1:
        name_card = card[:-17]
        card = str(card)[-16:]
        card_mask = card[:6] + "******" + card[12:]
        card_mask_finally = card_mask[:4] + " " + card_mask[4:8] + " " + card_mask[8:12] + " " + card_mask[12:]
        return f'{name_card} {card_mask_finally}'
    else:
        card = str(card)
    card_mask = card[:6] + "******" + card[12:]
    card_mask_finally = card_mask[:4] + " " + card_mask[4:8] + " " + card_mask[8:12] + " " + card_mask[12:]
    return f'{card_mask_finally}'


def get_mask_account(account: Union[int, str]) -> str:
    """Создаём маску счёта"""
    logger.info(f"Начало маскировки счёта: {account}")
    account = str(account)
    account_mask = "Счёт" + " " + "**" + account[-4:]
    return account_mask
