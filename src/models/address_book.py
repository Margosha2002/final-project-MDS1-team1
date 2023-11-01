from record import Record
from src.helpers.check_is_match import check_is_match


class ContactNotFoundError(Exception):
    pass


class AddressBook:
    data = []

    def add_contact(self, name, address, phone, birthday, email):
        record = Record(name, address, phone, birthday, email)
        self.data.append(record)

    def change_contact(self, name, field, value):
        record: Record = self.__get_contact(name)

        if field == "address":
            record.add_address(
                value.get("country"),
                value.get("city"),
                value.get("street"),
                value.get("house"),
            )
        elif field == "name":
            record.name = value
        elif field == "phone":
            record.phone = value
        elif field == "email":
            record.email = value
        elif field == "birthday":
            record.birthday = value

    def show_all(self):
        for item in self.data:
            print(str(item))

    def find_contacts(self, search):
        for record in self.data:
            if (
                check_is_match(record.name.value, search)
                or check_is_match(record.email.value, search)
                or check_is_match(record.phone.value, search)
            ):
                print(str(record))

    def __get_contact(self, name):
        for item in self.data:
            if item.name.value == name:
                return item

        raise ContactNotFoundError()

    def get_contact(self, name):
        print(str(self.__get_contact(name)))

    def delete_contact(self, name):
        self.data = list(filter(lambda item: item.name != name, self.data))

    def show_birthdays(self, days):
        for item in self.data:
            if item.check_birthday(days):
                print(str(item))
