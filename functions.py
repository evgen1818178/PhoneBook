


class phone_book:

    def __init__(self):
        self.database = []

    def to_list(self):
        len_list = len(self.database)
        output_list = []
        for number in range(len_list):
            output_list.append(self.database[number].to_dict())
        return output_list

    def from_list(self, list):
        self.database = []
        len_list = len(list)
        for number in range(len_list):
            cont = contact()
            self.database.append(cont.from_dict(list[number]))

    def add_contact(self):
        temp_contact = contact()
        temp_contact.name  = input("введите имя: ")
        temp_contact.phone = input("введите телефон: ")
        self.database.append(temp_contact)

    def find_from_name(self, name):
        len_list = len(self.database)
        for number in range(len_list):
            if self.database[number].name == name:
                return self.database[number].phone
        return "not on found"

    def find_from_phone(self, phone):
        len_list = len(self.database)
        for number in range(len_list):
            if self.database[number].phone == phone:
                return self.database[number].name
        return "not on found"

    def delete_from_name(self, name):
        len_list = len(self.database)
        for number in range(len_list):
            if self.database[number].name == name:
                self.database.pop(number)
                return "done"
        return "not on found"

    def delete_from_phone(self, phone):
        len_list = len(self.database)
        for number in range(len_list):
            if self.database[number].phone == phone:
                self.database.pop(number)
                return "done"
        return "not on found"

    def print(self):
        len_list = len(self.database)
        for number in range(len_list):
            print(self.database[number].name , "-", self.database[number].phone)





class contact:

    def __init__(self):
        self.name  = ""
        self.phone = ""

    def from_dict(self, dict):
        self.name = dict.get("name")
        self.phone = dict.get("phone")
        return self

    def to_dict(self):
        return_dict = {}
        return_dict.update({"name":  self.name})
        return_dict.update({"phone": self.phone})
        return return_dict