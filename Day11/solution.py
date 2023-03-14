from monkey import Monkey

def parse_input():
    monkeys = []
    with open("Day11/input.txt") as file:
        for line in file:
            monkey_n = line[7] # Monkey

            line = file.readline() # Starting items
            starting_items = [int(i) for i in line.replace(",", "").split()[2:]]

            line = file.readline() # Operation
            symbol = line[23]
            operand = line[25:] 
            operand = operand[:-1] # remove the /n from operand

            line = file.readline() # Test
            divisible_by = int(line[21:])

            line = file.readline() # True
            if_true = line[29]

            line = file.readline() # False
            if_false = line[30]

            line = file.readline() # Empty line

            monkeys.append(Monkey(monkey_n, starting_items, symbol, operand, divisible_by, if_true, if_false))
    return monkeys  


monkeys = parse_input()
for monkey in monkeys:
    print("\nMonkey ", monkey.monkey_n, ":")
    print(monkey.starting_items)
    monkey.print_operation()
    monkey.print_test()