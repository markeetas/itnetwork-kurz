"""Class that represents the entity insured """
class Insured:

    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name.ljust(5)}{self.surname.ljust(5)}{str(self.age).ljust(5)}{self.phone_number}"
