from operation import Operation
from test import Test

class Monkey:
    def __init__(self, monkey_n, starting_items, symbol, operand, divisible_by, if_true, if_false):
        self.monkey_n = monkey_n
        self.starting_items = starting_items
        self.operation = Operation(symbol, operand)
        self.test = Test(divisible_by, if_true, if_false)

    def print_operation(self):
        print(self.operation.symbol)
        print(self.operation.operand)

    def print_test(self):
        print(self.test.divisible_by)
        print(self.test.if_true)
        print(self.test.if_false)