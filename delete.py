import csv
from check import check_id


def delete_note():
    list = []
    del_id = int(input("Введите номер записи для удаления "))
    if check_id(del_id):
        with open("notes.csv", "r", encoding="utf-8") as d:
            data = csv.reader(d, delimiter=";", skipinitialspace=True)
            for rows in data:
                if int(rows[0]) != del_id:
                    list.append(";".join(rows))
        with open("notes.csv", "w+", encoding="utf-8") as f:
            for item in list:
                f.writelines(f"{item}\n")
        print("Удалено")
    else:
        print("Такой записи нет")
