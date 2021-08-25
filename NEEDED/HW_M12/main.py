import contact_book
import inspect
import pathlib
import signal
import sys


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f'Command {e} not found!!!'
        except ValueError as e:
            return e
        except IndexError as e:
            return f'Command not full!!'
    return inner


def com_add(name, phone, birthday=None):
    if name.value in [key.value for key in list(contact_list.keys())]:
        raise ValueError(f'The new contact cannot be saved because the name "{name.value}" already exists. '
                         f'Please enter a different name.\n')
    record = contact_book.Record(name, birthday) + phone
    contact_list.add_record(name, record)
    return f'New contact is saved: name "{name.value}", phone "{phone.value}", date of birth ' \
           f'"{birthday.value if birthday else "-"}".\n'


def com_change(name, phone, new_phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(
            f'Сontact by name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            for ph in rec.phones:
                if ph.value == phone:
                    rec.change_phone(ph, new_phone)
                    return f'Saved a new phone number "{new_phone.value}" for a contact with the name "{name}".\n'
                else:
                    raise ValueError(
                        f'The contact "{name}" does not have a phone number {phone}.\n')


def com_exit():
    return 'Good bye!\n'


def com_hello():
    return 'How can I help you?\n'


def com_join(name, phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(
            f'Сontact with name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            record = rec + phone
            contact_list.add_record(nam, record)
    return f'A new phone number "{phone.value}" has been added for the contact with the name "{name}".\n'


def com_delete(name, phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(
            f'Сontact by name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            for ph in rec.phones:
                if ph.value == phone:
                    rec.remove(ph)
                    return f'Delete phone number "{phone.value}" for a contact with the name "{name}".\n'
                else:
                    raise ValueError(
                        f'The contact "{name}" does not have a phone number {phone}.\n')


def com_phone(name):
    for nam, rec in contact_list.items():
        if nam.value == name:
            return ' '.join([phone.value for phone in rec.phones])
    raise ValueError(f'Contact with the name "{name}" does not exist.\n')


def com_show_all():
    return contact_list.iterator()


def com_search(pattern):
    result = ''
    for nam, rec in contact_list.items():
        phone_list = [phone.value for phone in rec.phones]
        for p in phone_list:
            if p.find(pattern) != (-1) or nam.value.find(pattern) != (-1):
                result += f'name: {nam.value}, phone: {" ".join([phone.value for phone in rec.phones])}, ' \
                          f'birtday: {rec.birthday.value if rec.birthday else "-"} ' \
                          f'{"("+str(rec.days_to_birthday())+" days)" if rec.days_to_birthday() else ""}\n'
    if not result:
        raise ValueError(f'No matches.\n')
    return result


@ input_error
def get_command_handler(user_input):
    if user_input[:2] == ['show', 'all']:
        return com_show_all()
    elif user_input[:2] == ['good', 'bye'] or user_input[0] in ('close', 'exit'):
        return com_exit()
    elif user_input[0] == 'search':
        return com_search(user_input[1])
    elif user_input[0] == 'hello':
        return com_hello()
    elif user_input[0] == 'phone':
        return com_phone(user_input[1])
    elif user_input[0] == 'delete':
        return com_delete(user_input[1], user_input[2])
    elif user_input[0] == 'join':
        return com_join(user_input[1], contact_book.Phone(user_input[2]))
    elif user_input[0] == 'add':
        birthday = contact_book.Birthday(
            user_input[3]) if len(user_input) > 3 else None
        return com_add(contact_book.Name(user_input[1]), contact_book.Phone(user_input[2]), birthday)
    elif user_input[0] == 'change':
        return com_change(user_input[1], user_input[2], contact_book.Phone(user_input[3]))
    else:
        raise KeyError(user_input[0])


def signal_handler(signal, frame):
    contact_list.save_dumped_data()
    sys.exit(0)


contact_list = contact_book.AddressBook()


if __name__ == '__main__':
    path = pathlib.Path('contact_list.txt')

    if path.exists() and path.stat().st_size > 0:
        contact_list = contact_list.read_dumped_data()

    while True:
        user_input = input(
            'Enter your command (hello, add, join, change, phone, search, delete, show all or exit/close/good bye):\n').lower().split()
        result = get_command_handler(user_input)
        if result == 'Good bye!\n':
            print(result)
            break
        elif inspect.isgenerator(result):
            for n in result:
                for rec in n:
                    print(f'name: {rec.name.value}; phone: {", ".join([phone.value for phone in rec.phones])}; '
                          f'birthday {rec.birthday.value if rec.birthday else "-"} '
                          f'{"("+str(rec.days_to_birthday())+" days)" if rec.days_to_birthday() else ""}. ')
        else:
            print(result)
            signal.signal(signal.SIGINT, signal_handler)

    serialized_list = contact_list.save_dumped_data()
