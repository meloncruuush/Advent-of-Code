def read_input_file():
    commands = []
    with open("Day10/input.txt", "r") as file:
        for line in file:
            commands.append(line.strip().split(" "))
    return commands


def print_commands(commands):
    for command in commands:
        print(command)


# ##### MAIN #####
commands = read_input_file()
# print_commands(commands)
cycle = 0
X = 1
next_cycle = 20
signal_strenghts = 0

for command in commands:
    if command[0] == "noop":
        cycle += 1
        if cycle == next_cycle:
            signal_strenghts += cycle * X
            next_cycle += 40
        continue

    if command[0] == "addx":
        cycle += 1
        if cycle == next_cycle:
            signal_strenghts += cycle * X
            next_cycle += 40

        cycle += 1
        if cycle == next_cycle:
            signal_strenghts += cycle * X
            next_cycle += 40
        X += int(command[1])

print("Signal strenght part 1: ", signal_strenghts)
