from datetime import datetime
from create import note_create
from read import print_note
from update import change_note
from delete import delete_note


def interface():
    print(
        "Это программа заметок. Выберите действие \
        \n 1 - создать заметку \n 2 - вывести заметку \
        \n 3 - редактировать заметку \n 4 - удалить заметку"
    )
    command = int(input("Введите номер операции "))
    while command not in [1, 2, 3, 4]:
        print("Неправильный ввод. Попробуйте еще раз ")
        command = int(input("Введите номер операции "))

    if command == 1:
        note_create()
    elif command == 2:
        print_note()
    elif command == 3:
        change_note()
    elif command == 4:
        delete_note()


if __name__ == "__main__":
    interface()
