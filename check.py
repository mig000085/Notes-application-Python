import csv


def check_id(num_id):
    flag = False
    with open("notes.csv", "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter=";", skipinitialspace=True)
        for row in data:
            if int(row[0]) == num_id:
                flag = True
                break
    return flag
