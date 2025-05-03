from calculate.view import View
from calculate.operators import Operators


class Controller:
    def __init__(self):
        self.operator = Operators()
        self.result = None

    def run(self):
        View.print_menu()
        is_home_menu_run = True
        while is_home_menu_run:
            input_msg = "Entrez votre choix"
            user_input = View.get_user_input(input_msg)
            if self._is_input_valid(user_input):
                self._operations(user_input)
                View.print_menu()
            is_home_menu_run = self._is_quit(user_input)
        View.end_message()

    def _is_input_valid(self, user_input):
        return user_input in ["1", "2", "3", "4"]

    def _operations(self, user_input):
        input_msg = "Entrez votre opération"
        operation = View.get_user_input(input_msg)

        if user_input == "1":
            self.result = self.operator.addition(operation)
        elif user_input == "2":
            self.result = self.operator.substraction(operation)
        elif user_input == "3":
            self.result = self.operator.multiplication(operation)
        elif user_input == "4":
            self.result = self.operator.division(operation)

        View.print_result(operation, self.result)
        View.continue_message()

    def _is_quit(self, user_input):
        return not user_input == "5"
