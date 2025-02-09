import pytest

from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize('card, expected_result', [
    (1111222233334444, '1111 22** **** 4444'),
    (2200700771792115, '2200 70** **** 2115'),
    (2202206862626137, '2202 20** **** 6137')
])
def test_get_mask_card_number(card, expected_result):
    assert len(get_mask_card_number(card)) == 19

    assert get_mask_card_number(card).count("*") == 6

    assert get_mask_card_number(card) == expected_result

@pytest.mark.parametrize('account, expected_result', [
    (73654108430135874305, '**4305'),
    (73654108430135871111, '**1111'),
    (73654108430135871234, '**1234')
])
def test_get_mask_account(account, expected_result):
    assert len(get_mask_account(73654108430135874305)) == 6

    assert get_mask_account(account) == expected_result
