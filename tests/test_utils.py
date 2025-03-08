from unittest.mock import patch

from src.utils import transaction_list

@patch('json.load')
def test_transaction_list(mock_result):
    mock_result.return_value = [{'1': 1}]
    assert transaction_list('data/operations.json') == [{'1': 1}]
    assert len(transaction_list('data/operations.json')) == 1
    mock_result.assert_called()