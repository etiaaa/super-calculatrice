class Operators:
    def __init__(self):
        self.operation = ""
        self.signe = ""
        self.result = 0.0

    def addition(self, operation):
        self.operation = operation
        self.signe = "+"
        if self._is_operation_valid():
            self._calculate_addition()
            return self.result

    def substraction(self, operation):
        self.operation = operation
        self.signe = "-"
        if self._is_operation_valid():
            self._calculate_substraction()
            return self.result

    def multiplication(self, operation):
        self.operation = operation
        self.signe = "*"
        if self._is_operation_valid():
            self._calculate_multiplication()
            return self.result

    def division(self, operation):
        self.operation = operation
        self.signe = "/"
        if self._is_operation_valid():
            self._calculate_division()
            return self.result

    def _is_operation_valid(self):
        if self._is_symbol_valid():
            self.numbers = self.operation.split(self.signe[0])
            for number in self.numbers:
                if not self._is_float(number):
                    return False
            return True
        return False

    def _is_symbol_valid(self):
        symbols = [symbol for symbol in self.operation if not symbol.isdigit()]
        for symbol in symbols:
            if symbol != self.signe and symbol != "." and symbol != " ":
                return False
        return True

    def _is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _calculate_addition(self):
        self.result = 0.0
        for number in self.numbers:
            self.result += float(number)

    def _calculate_substraction(self):
        self.result = float(self.numbers[0])
        for i in range(1, len(self.numbers)):
            self.result -= float(self.numbers[i])

    def _calculate_multiplication(self):
        self.result = 1.0
        for number in self.numbers:
            self.result *= float(number)

    def _calculate_division(self):
        self.result = float(self.numbers[0])
        for i in range(1, len(self.numbers)):
            try:
                self.result /= float(self.numbers[i])
            except ZeroDivisionError:
                self.result = None
