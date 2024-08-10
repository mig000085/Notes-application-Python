from datetime import datetime
import csv
def interface():
    print('Это программа заметок. Выберите действие \
        \n 1 - создать заметку \n 2 - вывести заметку \
        \n 3 - редактировать земетку \n 4 - удалить заметку')
    command = int(input('Введите номер операции '))
    while command!=1 and command!=2 and command!=3 and command!=4:
        print('Неправельный ввод. Попробуйте еще раз ')
        command = int(input('Введите номер операции '))
    if command == 1:
        note_create()
    elif command == 2:
        print_note()
    elif command == 3:
        change_note()
    elif command == 4:
        delete_note()

def note_create():
    id_notes = id_notes_list()
    title = input('Введите заголовок заметки ')
    note_body = input('Напишите вашу заметку ')
    date_time_create = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M")
    with open ('notes.csv', 'a', encoding='utf-8') as f:
        f.write(f'{id_notes};{title};{note_body};{date_time_create}\n')
def id_notes_list():
    with open ('notes.csv', 'r', encoding='utf-8') as f:
        count = 1
        list =[]
        flag =True        
        with open ('notes.csv', 'r', encoding='utf-8') as f:
            data = csv.reader(f, delimiter=';', skipinitialspace=True)
            for row in data:
                list.append(int(row[0]))            
            while flag:
                if count in list:
                    count+=1
                else:
                    flag = False                    
            return count
        def print_note():
    #разные варианты вывода
    print("Вывести все заметки - 1\nвывод заметки по номеру - 2\nвывод заметок по дате - 3")
    command = int(input('Введите номер операции '))
    while command!=1 and command!=2 and command!=3:
        print('Неправельный ввод. Попробуйте еще раз ')
        command = int(input('Введите номер операции '))
    if command == 1:
        with open ('notes.csv', 'r', encoding='utf-8') as f:
            data = csv.reader(f, delimiter=';', skipinitialspace=True)
            for row in data:
                print(f'Номер записи: {row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}')
    elif command == 2:
        num_id = int(input('Введите номер заметки для просмотра '))
        if check_id(num_id):
            with open ('notes.csv', 'r', encoding='utf-8') as f:
                data = csv.reader(f, delimiter=';', skipinitialspace=True)
                for row in data:
                    if int(row[0]) == num_id:
                        print(f'Номер записи: {row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}')
        else:
            print('Такой записи нет')
    elif command == 3:
        time_note = input('Введите дату создания в формате ДД.ММ.ГГГГ ')
        with open ('notes.csv', 'r', encoding='utf-8') as f:
            data = csv.reader(f, delimiter=';', skipinitialspace=True)
            for row in data:
                if row[3][:10] == time_note:
                    print(f'Номер записи: {row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}')

        