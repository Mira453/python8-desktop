class FiniteAutomaton:
    def __init__(self):
        # Початковий стан
        self.state = "S0"
        # Кількість одиниць
        self.count_ones = 0

    def transition(self, input_symbol):
        if self.state == "S0":
            if input_symbol == "0":
                self.state = "S0"
            elif input_symbol == "1":
                self.count_ones += 1
                self.state = "S1"
            elif input_symbol == "Q":
                return self.check_parity()

        elif self.state == "S1":
            if input_symbol == "0":
                self.state = "S0"
            elif input_symbol == "1":
                self.count_ones += 1
                self.state = "S1"
            elif input_symbol == "Q":
                return self.check_parity()

        else:
            raise ValueError("Invalid state")

    def check_parity(self):
        # Перевірка парності кількості одиниць
        return "P" if self.count_ones % 2 == 0 else "N"

    def process_string(self, input_string):
        output = []
        for symbol in input_string:
            if symbol not in {"0", "1", "Q"}:
                raise ValueError(f"Invalid input symbol: {symbol}")

            result = self.transition(symbol)
            if result is not None:
                output.append(result)

        return output

# Приклад використання
if __name__ == "__main__":
    automaton = FiniteAutomaton()
    input_string = input("Введіть ланцюжок (0, 1, Q): ")

    try:
        output = automaton.process_string(input_string)
        print("Результат роботи автомата:", output)
    except ValueError as e:
        print("Помилка:", e)