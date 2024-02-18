"""Trida reprezentujici evidenci pojistenych"""
class Register:
    def __init__(self):
        self.insured = []

    def add_insured(self, insured):
        """Method that adds insured specified by parameter 'insured'"""
        self.insured.append(insured)

    def display_insured(self):
        """Method that displays all insured"""
        for insured in self.insured:
            print(insured)

    def find_insured(self, name, surname):
        """Method that finds insured
         specified by parameters 'name', 'surname'"""
        for insured in self.insured:
            if insured.name == name and insured.surname == surname:
                return insured
        return None
