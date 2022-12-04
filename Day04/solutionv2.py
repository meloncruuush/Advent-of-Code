def line_to_range(line):
    pass

with open('Day04/input.txt') as file:
    for line in file:
        replaced_line = line.replace(',' , '-')
        a = [int(s) for s in replaced_line.split('-')]
        print(a)

        