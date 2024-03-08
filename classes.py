from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        Field.__init__(self, name)
        self.name = name

class Birthday:
    def __init__(self, value: str):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            print("The birthday date must be in format DD.MM.YYYY")
            raise

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone_number(value):
            raise ValueError("Invalid phone number format")
        self.value = value

    @staticmethod
    def validate_phone_number(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def delete_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        for i, _ in enumerate(self.phones):
            if str(self.phones[i]) == old_phone_number:
                self.phones[i] = Phone(new_phone_number)
                break

    def find_old_phone(self):
        old_phone = str(self.phones[0])
        return(old_phone)

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, user_name):
        for phone in self.phones:
            if phone.value == user_name:
                return phone.value
            raise ValueError("Phone number not found")

    def add_birthday(self, birthday):
        birthday = Birthday(birthday)
        self.birthday = birthday
        return(self.birthday)

    def show_birthday(self):
        birthday = str(self.birthday.date)
        return (birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, value):
        if not (self.data.get(value)):
            print("There is not such name in AddressBook")
            raise ValueError
        return(self.data.get(value))

    def delete(self, name):
        del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.now()
        end_of_week = today + timedelta(days=(6 - today.weekday()))
        birthdays_this_week = []
        for record in self.data.values():
            if record.birthday and record.birthday.date:
                birthday_date = record.birthday.date.replace(year=today.year)
                if today <= birthday_date <= end_of_week:
                    birthdays_this_week.append(record.name.value)
        return birthdays_this_week