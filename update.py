from datetime import datetime  # Импортируем модуль datetime
import csv
from check import check_id


def change_note():
    list = []
    change_id = int(input("Введите номер записи для изменения "))
    if check_id(change_id):
        with open("notes.csv", "r", encoding="utf-8") as d:
            data = csv.reader(d, delimiter=";", skipinitialspace=True)
            for rows in data:
                if int(rows[0]) != change_id:
                    list.append(";".join(rows))
                else:
                    id_notes = rows[0]
                    title = input("Измените заголовок заметки ")
                    note_body = input("Измените текст заметки ")
                    date_time_create = datetime.strftime(
                        datetime.now(), "%d.%m.%Y %H:%M"
                    )
                    list.append(f"{id_notes};{title};{note_body};{date_time_create}")
        with open("notes.csv", "w+", encoding="utf-8") as f:
            for item in list:
                f.writelines(f"{item}\n")
        print("Изменено")
    else:
        print("Такой записи нет")
