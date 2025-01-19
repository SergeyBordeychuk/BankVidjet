def mask_account_card(card) -> str:
    if 'Счет' in card:
        return f'Счет **{card[-4:]}'
    else:
        return f'{card[:-17]} {card[-17:-12]} {card[-12:-10]}** **** {card[-4:]}'

print(mask_account_card('Visa Platinum 7000792289606361'))