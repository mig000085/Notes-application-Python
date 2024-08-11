from datetime import datetime
import csv


def note_create():
    id_notes = id_notes_list()
    title = input("Введите заголовок заметки ")
    note_body = input("Напишите вашу заметку ")
    date_time_create = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M")
    with open("notes.csv", "a", encoding="utf-8") as f:
        f.write(f"{id_notes};{title};{note_body};{date_time_create}\n")


def id_notes_list():
    with open("notes.csv", "r", encoding="utf-8") as f:
        count = 1
        list = []
        flag = True
        data = csv.reader(f, delimiter=";", skipinitialspace=True)
        for row in data:
            list.append(int(row[0]))
        while flag:
            if count in list:
                count += 1
            else:
                flag = False
        return count
