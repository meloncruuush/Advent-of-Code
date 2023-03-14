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


def print_monkeys(monkeys):
    for monkey in monkeys:
        print("\nMonkey ", monkey.monkey_n, ":")
        print(monkey.starting_items)
        monkey.print_operation()
        monkey.print_test()


monkeys = parse_input()
print_monkeys(monkeys)

rounds = 0
while rounds < 20:
    for monkey in monkeys:
        for item_worrylvl in monkey.starting_items:

            # Monkey inspects item
            if monkey.get_operand() != "old":
                if monkey.get_symbol() == "+":
                    item_worrylvl = item_worrylvl + int(monkey.get_operand())
                else:
                    item_worrylvl = item_worrylvl * int(monkey.get_operand())
                    
            else:
                if monkey.get_symbol() == "+":
                    item_worrylvl = item_worrylvl + item_worrylvl
                else:
                    item_worrylvl = item_worrylvl * item_worrylvl

            # Decrease worry level
            item_worrylvl = item_worrylvl // 3

            # Throw item to other monkey
            if item_worrylvl % monkey.get_divisible_by() == 0:
                index = monkey.get_when_true()
                monkeys[index-1].starting_items.append(item_worrylvl)
            else:
                index = monkey.get_when_false()
                monkeys[index].starting_items.append(item_worrylvl)
