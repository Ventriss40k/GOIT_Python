from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record.phones



class Record():
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, phone, new_phone):
        current = self.phones.index(phone)
        self.phones[current] = new_phone


class Field():
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone




