from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Birthday():
    def __init__(self, date_str: str):
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD.MM.YYYY")
        self.date_str = date_str

class Name(Field):
    def __init__(self, value: str):
        if not value.isalpha():
            print("The name must consist letters only")
            raise ValueError
        if not value.istitle():
            print("The name must start with an upper case letter and the rest letter must be lower case")
            raise ValueError
        self.value = value


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
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def delete_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        for i, _ in enumerate(self.phones):
            if str(self.phones[i]) == old_phone_number:
                self.phones[i] = Phone(new_phone_number)
                break

    def find_phone(self, user_name):
        for phone in self.phones:
            if phone.value == user_name:
                return phone.value
            raise ValueError("Phone number not found")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return self.birthday

    def __str__(self):
        phones = '; '.join(str(phone) for phone in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, value):
        return(self.data.get(value))

    def delete(self, name):
        del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.now()
        end_of_week = today + timedelta(days=(6 - today.weekday()))
        birthdays_this_week = []
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.date.replace(year=today.year)
                if today <= birthday_date <= end_of_week:
                    birthdays_this_week.append(record.name.value)
        return birthdays_this_week


