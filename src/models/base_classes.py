import re
from datetime import datetime
from .exceptions import (
    PhoneValidationError,
    BirthdayValidationError,
    EmailValidationError,
    NameIsRequiredException,
    BodyValidationError,
    TagValidationError,
)


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if not name:
            raise NameIsRequiredException()
        super().__init__(name)


class Body(Field):
    def __init__(self, value):
        if not value:
            raise BodyValidationError()
        super().__init__(value)


class Tag(Field):
    def __init__(self, value):
        if not value:
            raise TagValidationError()
        super().__init__(value)


class Phone(Field):
    def __init__(self, phone):
        # acceptable formats 1111111111, (111)111-1-111, 111-111-11-11, (111)111-11-11
        valid_phone_number = re.match(
            r"(^[(]?[\d]{3}[)\-]?[\d]{3}[-]?[\d]{2}[-]?[\d]{2}$)|(^[(]?[\d]{3}[)\-]?[\d]{3}[-]?[\d]{1}[-]?[\d]{3}$)",
            phone,
        )

        if not valid_phone_number:
            raise PhoneValidationError()

        super().__init__(phone)


class Birthday(Field):
    def __init__(self, birthday):
        # acceptable format "DD.MM.YYYY"
        valid_format = re.match(
            r"^(0[1-9]|1\d|2\d|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$", birthday
        )

        if not valid_format:
            raise BirthdayValidationError()

        birthday_date = datetime.strptime(birthday, "%d.%m.%Y").date()
        super().__init__(birthday_date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Email(Field):
    def __init__(self, email):
        valid_email = re.match(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$", email)

        if not valid_email:
            raise EmailValidationError()

        super().__init__(email)


class Address:
    def __init__(
        self,
        country,
        city,
        street,
        house,
    ):
        self.country = country
        self.city = city
        self.street = street
        self.house = house

    def __str__(self):
        return f"{ self.country}, {self.city}, {self.street} street, {self.house}"
