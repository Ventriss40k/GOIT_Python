import pickle

from addressbook import Record, AddressBook, Name, Phone, ViewAbcInterface

DEFAULT_ADDRESS_BOOK_PATH = ".address_book.bin"


def dump_address_book(path, address_book):
    with open(path, "wb") as f:
        pickle.dump(address_book, f)


def load_address_book(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

class Commands(ViewAbcInterface):
    commands_list = ["add", "exit", "delete", "show"]
    def view_console():
        print(Commands.commands_list)

if __name__ == "__main__":
    # commands = ["add", "exit", "edit", "delete", "show"]
    address_book = load_address_book(DEFAULT_ADDRESS_BOOK_PATH)
    while True:
        command = input("Choose command:> ")
        if command == "add":
            name = input("Input name: ")
            phone = input("Input phone: ")
            record = Record(Name(name), [Phone(phone)])
            address_book.add(record)
        elif command == "show":
            for page in address_book.iterator(2):
                print(page)
        elif command == "edit":
            name = input("Input name: ")
            old_phone = input("Input old phone: ")
            new_phone = input("Input new phone: ")
            old_record = Record(Name(name), [Phone(old_phone)])
            new_record = Record(Name(name), [Phone(new_phone)])
            address_book.edit_record(old_record, new_record)
        elif command == "delete":
            name = input("Input name: ")
            phone = input("Input phone: ")
            record = Record(Name(name), [Phone(phone)])
            address_book.delete(record)
        elif command == "exit":
            print("Bye!")
            dump_address_book(DEFAULT_ADDRESS_BOOK_PATH, address_book)
            break
        else:
            print(f"Unrecognized command: {command}")
            print(f"Available commands: {Commands.commands_list}")
