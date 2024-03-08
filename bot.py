# -*- coding: utf-8 -*-

'''
Сommands:

1) add [Name] [Phone]                      Add new contact with a "Name" and "Phone number".
2) change [Name] [New phone]               Change phone number to "New phone" for contact with "Name".
3) phone [Name]                            Show phohne number for contact "Name".
4) all                                     Show all contacts in AddressBook.
5) add-birthday [Name] [Date of Birth]     Add "Date of Birth" for contact "Name".
6) show-birthday [Name]                    Show Date of Birth for contact "Name".
7) birthdays                               Show all birthdays for the next week.
8) hello                                   Receive "Hello" from the bot.
9) close OR exit                           Close the program.
10) help                                   Get this list of commands.
'''

from classes import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_contact(args, contacts):
    name = args[0].lower()  # Перетворення імені на нижній регістр
    for contact_name, phone in contacts.items():
        if contact_name.lower() == name:
            return phone
        return "Contact not found."

@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    if name in contacts:
        record = contacts[name]
        if not record.birthday:
            record.add_birthday(birthday)
            return "Birthday added."
        else:
            return "Birthday already exists for this contact."
    else:
        return "Contact not found."
    
    
@input_error
def birthdays(contacts):
    upcoming_birthdays = contacts.get_birthdays_per_week()
    if not upcoming_birthdays:
        return "No upcoming birthdays this week."
    return "Upcoming birthdays:\n" + "\n".join(upcoming_birthdays)
    
@input_error
def show_birthday(args, contacts):
    name = args[0]
    if name in contacts:
        record = contacts[name]
        if record.birthday:
            return f"{name}'s birthday is on {record.birthday}"
        else:
            return f"{name} doesn't have a birthday set."
    else:
        return "Contact not found."

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        command = command.lower()  # Приведення команди до нижнього регістру

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()