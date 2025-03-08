import csv

import pandas as pd


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
    excel_dict = excel_file.to_dict(orient='records')
    return excel_dict
