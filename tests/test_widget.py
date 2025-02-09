import pytest

from src.widget import mask_account_card, get_date

@pytest.mark.parametrize('card, expected_result', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658')
])
def test_mask_account_card(card, expected_result):
    assert mask_account_card(card) == expected_result

    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'

@pytest.mark.parametrize('date, expected_result', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-02-08T02:26:18.671407', '08.02.2025'),
    ('2007-09-29T02:26:18.671407', '29.09.2007')
])
def test_get_date(date, expected_result):
    assert get_date(date) == expected_result

    assert len(get_date(date)) == 10