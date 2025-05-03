class View:
    @staticmethod
    def print_menu():
        print("\n=========== MENU ===========")
        print("1 - Addition")
        print("2 - Soustraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Quitter")
        print("============================\n")

    @staticmethod
    def get_user_input(input_msg):
        user_input = input(f"{input_msg} : ")
        return user_input

    @staticmethod
    def end_message():
        print("=========== GOOD-BYE ===========")

    @staticmethod
    def continue_message():
        input("Appuyez sur ENTRER pour continuer ...")

    @staticmethod
    def print_result(operation, result):
        if result is not None:
            print(f"RESULTAT : {operation} = {result}")
        else:
            print("Votre operation est incorrect ! : "
                  f"{operation}")
