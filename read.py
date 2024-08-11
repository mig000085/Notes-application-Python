import csv
from check import check_id


def print_note():
    print(
        "Вывести все заметки - 1\nвывод заметки по номеру - 2\nвывод заметок по дате - 3"
    )
    command = int(input("Введите номер операции "))
    while command not in [1, 2, 3]:
        print("Неправильный ввод. Попробуйте еще раз ")
        command = int(input("Введите номер операции "))

    if command == 1:
        with open("notes.csv", "r", encoding="utf-8") as f:
            data = csv.reader(f, delimiter=";", skipinitialspace=True)
            for row in data:
                print(
                    f"Номер записи: {row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}"
                )
    elif command == 2:
        num_id = int(input("Введите номер заметки для просмотра "))
        if check_id(num_id):
            with open("notes.csv", "r", encoding="utf-8") as f:
                data = csv.reader(f, delimiter=";", skipinitialspace=True)
                for row in data:
                    if int(row[0]) == num_id:
                        print(
                            f"Номер записи: {row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}"
                        )
        else:
            print("Такой записи нет")
    elif command == 3:
        time_note = input("Введите дату создания в формате ДД.ММ.ГГГГ ")
        with open("notes.csv", "r", encoding="utf-8") as f:
            data = csv.reader(f, delimiter=";", skipinitialspace=True)
            for row in data:
                if row[3][:10] == time_note:
                    print(
                        f"Номер записи: {row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}"
                    )
