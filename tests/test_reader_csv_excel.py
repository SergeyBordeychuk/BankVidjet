from unittest.mock import patch, Mock

from src.reader_csv_excel import reader_csv, reader_excel
import pandas as pd

@patch('csv.DictReader')
def test_reader_csv(mock_result):
    mock_result.return_value = [{'1':'2'},{'3':'4'}]
    assert reader_csv('data/transactions.csv') == [{'1':'2'},{'3':'4'}]
    assert len(reader_csv('data/transactions.csv')) == 2
    mock_result.assert_called()


def test_reader_excel():
    assert len(reader_excel('data/transactions_excel.xlsx')) == 1000

