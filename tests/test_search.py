from unittest.mock import patch

from src.search import search_operations


@patch('re.search')
def test_search_operations(mock_result):
    mock_result.return_value = [{'description': '1'}, {'description': 'Перевод 1'}]
    assert search_operations([{'description':'1'}, {'description':'Перевод 1'}], '1') == [{'description': '1'}, {'description': 'Перевод 1'}]
    assert len(search_operations([{'description': '1'}, {'description': 'Перевод 1'}], '1')) == 2
    mock_result.assert_called()