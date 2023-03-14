from monkey import Monkey

def parse_input():
    with open("Day11/input.txt") as file:

        line = file.readline() # Monkey
        monkey_n = line[7]

        line = file.readline() # Starting items
        # remove any commas in the line, then read the numbers from the line and put them in a list
        starting_items = [int(i) for i in line.replace(",", "").split()[2:]]

        line = file.readline() # Operation
        

        line = file.readline() # Test
        line = file.readline() # True
        line = file.readline() # False
        line = file.readline() # Empty line

        # monkey = Monkey(monkey_n, starting_items, symbol, operand, divisible_by, if_true, if_false)







parse_input()