import time
from time import sleep

from src.external_api import amount_transition
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.reader_csv_excel import reader_csv, reader_excel
from src.search import search_operations
from src.utils import transaction_list


def main():
    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
            ''')
    while True:
        first_message_user = int(input('Введите пункт: '))
        if first_message_user == 1:
            print('Для обработки выбран JSON-файл.')
            path = str(input('Введите путь к файлу: '))
            operations = transaction_list(path)
            break
        elif first_message_user == 2:
            print('Для обработки выбран CSV-файл.')
            path = str(input('Введите путь к файлу: '))
            operations = reader_csv(path)
            break
        elif first_message_user == 3:
            print('Для обработки выбран XLSX-файл.')
            path = str(input('Введите путь к файлу: '))
            operations = reader_excel(path)
            break
        else:
            print('Неверный пункт меню')
            print('Введите пункт заново')

    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

        second_message_user = input('Необходимый статус: ').upper()

        if second_message_user == ("EXECUTED" or "CANCELED" or "PENDING"):
            print(f'Операции отфильтрованы по статусу "{second_message_user}"')
            sorted_operations_by_state = filter_by_state(operations, second_message_user)
            break
        else:
            print(f'Статус операции "{second_message_user}" недоступен.')

    sorted_by_date= input('Отсортировать операции по дате? Да/Нет: ').lower()
    reverse = input('Отсортировать по возрастанию или по убыванию?: ').lower()
    rub = input('Выводить только рублевые тразакции? Да/Нет: '.lower())
    exclude_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').lower()

    if sorted_by_date == 'да' and reverse == 'по возрастанию':
        print('Сортируем по дате и возрастанию...')
        new_operations = sort_by_date(sorted_operations_by_state, revers=False)
    elif sorted_by_date == 'да' and reverse == 'по убыванию':
        print('Сортируем по дате и убыванию...')
        new_operations = sorted_operations_by_state
    elif sorted_by_date == 'нет' and reverse == 'по возрастанию':
        print('Сортируем по возрастанию...')
        new_operations = list(sorted(sorted_operations_by_state, reverse=True))
    elif sorted_by_date == 'нет' and reverse == 'по убыванию':
        print('Сортируем по убыванию...')
        new_operations = sorted(sorted_operations_by_state, reverse=False)

    if rub == 'да':
        print('Меняем валюты...')
        amount = []
        for operation in new_operations:
             amount.append(amount_transition(operation))

    if exclude_word == 'да':
        word = input('Введите слово: ')
        print('Фильтруем по слову...')
        new_operations = search_operations(new_operations, word)

    print('Распечатываю итоговый список транзакций...')
    time.sleep(3)
    if len(new_operations) != 0:
        print(f'Всего банковских операций в выборке: {len(new_operations)}')
        for operations in new_operations:
            if operations['to'][:4] == 'Счет':
                second_card = get_mask_account(operations['to'])
            else:
                second_card = get_mask_card_number(operations['to'])
            if operations['from'][:4] == 'Счет':
                first_card = get_mask_account(operations['from'])
            else:
                first_card = get_mask_card_number(operations['from'])
            date_fu = operations['date']
            date = f'{date_fu[8:10]}.{date_fu[5:7]}.{date_fu[:4]}'
            if operations['descritpion'] == 'Открытие влада':
                print(f'''\n{date} Открытие вклада
                {second_card}
                Сумма: {operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}
                ''')
            else:
                print(f'''\n{date} {operations['descreption']}
                            {first_card} -> {second_card}
                            Сумма: {operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}
                ''')
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')



if __name__ == '__main__':
    main()