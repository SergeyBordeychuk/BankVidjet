import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card: Union[int, str]) -> str:
    """Создаём маску карты"""
    logger.info(f"Начало маскировки номера карты: {card}")
    card = str(card)
    card_mask = card[:6] + "******" + card[12:]
    return card_mask[:4] + " " + card_mask[4:8] + " " + card_mask[8:12] + " " + card_mask[12:]


def get_mask_account(account: Union[int, str]) -> str:
    """Создаём маску счёта"""
    logger.info(f"Начало маскировки счёта: {account}")
    account = str(account)
    account_mask = "**" + account[-4:]
    return account_mask
