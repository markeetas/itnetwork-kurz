from insured import Insured
from helper import Helper


"""Class that represents user interface"""
class UserInterface:
    def __init__(self, register):
        self.register = register

    def add_insured(self):
        """Method that represents the process of adding insured"""
        name = Helper.custom_input("Zadejte jméno pojištěného: ")
        surname = Helper.custom_input("Zadejte příjmení: ")
        age = Helper.custom_input("Zadejte věk: ")
        phone_number = Helper.custom_input("Zadejte telefonní číslo: ")

        insured = Insured(name, surname, age, phone_number)
        self.register.add_insured(insured)
        print("\nData byla uložena. Pokračujte libovolnou klávesou...")
        input()

    def display_insured(self):
        """Method that that represents the process of displaying all insured"""
        print("--------------------")
        print("Evidence pojištěných")
        print("---------------------")
        self.register.display_insured()
        print("\nPokračujte libovolnou klávesou...")
        input()

    def find_insured(self):
        """Method that that represents the process of finding specified insured"""
        name = Helper.custom_input("Zadejte jméno pojištěného: ")
        surname = Helper.custom_input("Zadejte příjmení: ")

        found = self.register.find_insured(name, surname)

        if found:
            print("\n-----------------")
            print("Evidence pojištěných")
            print("--------------------------")
            print(found)
            print("\nPokračujte libovolnou klávesou...")
            input()
        else:
            print("\nPojištěnec nenalezen. Pokračujte libovolnou klávesou...")
            input()





