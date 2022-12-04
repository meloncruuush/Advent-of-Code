def contained_in_range(assignments):
    if assignments[0] >= assignments[2] and assignments[1] <= assignments[3]:
        return 1
    elif assignments[2] >= assignments[0] and assignments[3] <= assignments[1]:
        return 1
    return 0

def line_converter(line):
    replaced_line = line.replace(',' , '-')
    return [int(s) for s in replaced_line.split('-')]

def check_overlap(line):
    return 0


with open('Day04/input.txt') as file:
    sum_p1 = 0
    sum_p2 = 0
    for line in file:
        assignments = line_converter(line)
        sum_p1 += contained_in_range(assignments)
        sum_p2 += check_overlap(assignments)

    print("Result 1: " + str(sum_p1))