import pytest

from src.sort_operation import sort_operations

@pytest.mark.parametrize('list_dict, category, expected_result, leng', [
    ([{'description': 'Супермаркет'},{'description': 'Такси'},{'description': 'Супермаркет'},{'description': 'Кинотеатры'}], ['Супермаркет','Такси'], {'Супермаркет': 2, 'Такси': 1}, 2),
    ([{'description': 'Супермаркет'},{'description': 'Такси'},{'description': 'Супермаркет'},{'description': 'Кинотеатры'},{'description': 'Такси'},{'description': 'Такси'}], ['Супермаркет','Такси'], {'Супермаркет': 2, 'Такси': 3}, 2)
])
def test_sort_operations(list_dict,category,expected_result, leng):
    assert sort_operations(list_dict, category) == expected_result
    assert len(sort_operations(list_dict, category)) == leng
