from operation import Operation
from test import Test

class Monkey:
    def __init__(self, monkey_n, starting_items, symbol, operand, divisible_by, when_true, when_false):
        self.monkey_n = monkey_n
        self.starting_items = starting_items
        self.operation = Operation(symbol, operand)
        self.test = Test(divisible_by, when_true, when_false)

    def print_operation(self):
        print(self.operation.symbol)
        print(self.operation.operand)

    def print_test(self):
        print(self.test.divisible_by)
        print(self.test.when_true)
        print(self.test.when_false)

    def get_symbol(self):
        return self.operation.symbol
    
    def get_operand(self):
        return self.operation.operand
    
    def get_divisible_by(self):
        return int(self.test.divisible_by)

    def get_when_true(self):
        return int(self.test.when_true)

    def get_when_false(self):
        return int(self.test.when_false)