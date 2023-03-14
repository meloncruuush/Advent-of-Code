from operation import Operation
from test import Test

class Monkey:
    def __init__(self, monkey_n, starting_items, symbol, operand, divisible_by, if_true, if_false):
        self.monkey_n = monkey_n
        self.starting_items = []
        self.operation = Operation(symbol, operand)
        self.test = Test(divisible_by, if_true, if_false)