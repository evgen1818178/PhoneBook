from functions import phone_book
import json
import os.path

path_to_file = "book.json"

check_file = os.path.exists(path_to_file)  # True


book = phone_book()

if check_file:

    with open(path_to_file, "r") as file:
        book.from_list(json.load(file))
        file.close()

else:
    user_string = input("Книга не найдена, создать? (y/n) ")
    if user_string != "y":
        exit()




user_string = ""
while user_string != "exit":
    user_string = input("Введите команду: ")

    if user_string == "help":
        print("add         - добавить номер в книгу")
        print("get name    - узнать имя по номеру")
        print("get phone   - узнать телефон по имени")
        print("del f name  - удалить запись по имени")
        print("del f phone - удалить запись по номеру")
        print("print       - показать содержимое книги")

    if user_string == "add":
        book.add_contact()

    if user_string == "get name":
        user_string = input("Введите номер: ")
        print("name is:", book.find_from_phone(user_string))

    if user_string == "get phone":
        user_string = input("Введите имя: ")
        print("phone is:", book.find_from_name(user_string))

    if user_string == "del f name":
        user_string = input("Введите имя: ")
        print(book.delete_from_name(user_string))

    if user_string == "del f phone":
        user_string = input("Введите номер: ")
        print(book.delete_from_phone(user_string))

    if user_string == "print":
        book.print()





if check_file:
    os.remove(path_to_file)

with open(path_to_file, "w") as file:
    json.dump(book.to_list(), file)
    file.close()