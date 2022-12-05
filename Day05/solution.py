def get_crates_from_file(file):
    crates = []
    for line in file:
        if line == '\n':
            break
        i = 1
        array = []
        while i < len(line):
            array.append(line[i])
            i += 4
        crates.append(array)
    return crates


def get_moves_from_file(file):
    # moves = []
    # for line in file:
    #     digits = []
    #     for c in line:
    #         if c.isdigit():
    #             digits.append(c)
    #     moves.append(digits)
    # return moves
    moves = []
    for line in file:
        moves.append([int(s) for s in line.split() if s.isdigit()])
    return moves


def rotate_crates(crates_raw):
    crates_tuples = list(zip(*crates_raw[::-1]))
    return [list(ele) for ele in crates_tuples]


def print_matrix(message, matrix):
    print("\n" + message)
    for row in matrix:
        print(row)


def remove_empty(crates):
    for i in range(len(crates)):
        to_pop = 0
        for element in crates[i]:
            if element == ' ':
                to_pop += 1

        while to_pop > 0:
            crates[i].pop()
            to_pop -= 1

    return crates


def arrange_crates(crates, moves):
    for move in moves:
        # move 1 from 2 to 1
        n_crates = move[0]
        pos1 = move[1]-1
        pos2 = move[2]-1

        while n_crates > 0:
            crates[pos2].append(crates[pos1].pop())
            n_crates -= 1
    return crates


with open('Day05/input.txt') as file:
    crates_raw = get_crates_from_file(file)
    print_matrix("Crates row: ", crates_raw)

    crates_rotated = rotate_crates(crates_raw)
    print_matrix("Crates rotated: ", crates_rotated)

    crates = remove_empty(crates_rotated)
    print_matrix("Crates without empty cells: ", crates)

    moves = get_moves_from_file(file)
    print_matrix("Moves: ", moves)

    arranged_crates = arrange_crates(crates, moves)
    print_matrix("Arranged crates: ", arranged_crates)

    print("\nResult: ")
    for row in arranged_crates:
        print(row[len(row)-1], end='')
