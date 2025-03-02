import csv

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


def reader_csv(path: str) -> list:
    """Функция считывает финансовые операции csv файлов"""
    file_result = []
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            file_result.append(row)
        return file_result


def reader_excel(path: str):
    """Функция считывает финансовые операции excel файлов"""
    excel_file = pd.read_excel(path)
    list_excel = excel_file.to_dict(orient='records')
    return list_excel
