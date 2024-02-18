"""Main program"""
from user_interface import UserInterface
from register import Register


def run_program():
    evidence = Register()
    ui = UserInterface(evidence)

    choice = ""
    while choice != "4":
        print("\n--------------------")
        print("Evidence pojištěných")
        print("----------------------")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Zobrazit všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        choice = input().strip()

        if choice == "1":
            ui.add_insured()
        elif choice == "2":
            ui.display_insured()
        elif choice == "3":
            ui.find_insured()
        elif choice == "4":
            print("Konec.")
        else:
            print(f"Nevalidní vstup: {choice}")


if __name__ == "__main__":
    run_program()
