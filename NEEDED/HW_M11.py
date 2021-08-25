from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self):
        self.__value = None


class Name(Field):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        super().__init__()
        self.phone = phone

    @property
    def phone(self):
        return self.__value

    @phone.setter
    def phone(self, phone):
        if phone.isdigit():
            self.__value = phone
        else:
            raise Exception('Please, enter a valid phone number')


class Birthday(Field):
    def __init__(self, birthday):
        super().__init__()
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__value

    @birthday.setter
    def birthday(self, birthday):
        if birthday.isdigit() and len(birthday) == 8:
            birth_day = datetime(year=int(birthday[4:]), month=int(
                birthday[2:4]), day=int(birthday[0:2]))
            self.__value = birth_day.replace(datetime.now().year)
        else:
            raise Exception('Please, enter a valid date birthday')


class Record:
    def __init__(self, name, birthday=None):
        self.name = name
        self.phones = []
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, phone, new_phone):
        current = self.phones.index(phone)
        self.phones[current] = new_phone

    def days_to_birthday(self):
        if self.birthday:
            if self.birthday.birthday.month >= datetime.now().month:
                return self.birthday.birthday.date() - datetime.now().date()
            else:
                birth_day = datetime(year=self.birthday.birthday.year + 1, month=self.birthday.birthday.month,
                                     day=self.birthday.birthday.day).date()
                return birth_day - datetime.now().date()
        else:
            raise Exception("Please, add a birthday date")


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record.phones

    def __iter__(self):
        return self

    def __next__(self):
        counter = 0
        for key, value in self.data.items():
            if counter == len(self):
                raise StopIteration
            else:
                counter += 1
                return key, value
