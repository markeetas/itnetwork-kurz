"""Helper class"""
class Helper:
    @staticmethod
    def custom_input(string_to_show):
        """Method that wraps classic input and adds the trim + empty value validation
        string_to_show represents first parameter of classic input"""
        value = input(string_to_show).strip()
        if (value == ""):
            print("Hodnota je povinná. Zadejte prosím znovu.")
            return Helper.custom_input(string_to_show)
        return value