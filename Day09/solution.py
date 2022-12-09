def read_input_file():
    with open('Day09/input.txt') as file:
        moves = []
        for line in file:
            moves.append(line.strip().split(' '))
        return moves


def print_moves(moves):
    for move in moves:
        print(move)


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def create_matrix():
    # create a 20 by 20 matrix filled with dots
    matrix = []
    for i in range(20):
        matrix.append([])
        for j in range(20):
            matrix[i].append('.')

    matrix[len(matrix) - 1][0] = 'H'
    return matrix


def right_move(matrix, H_pos, T_pos):
    if H_pos[0] == T_pos[0]:
         
    
    return matrix, H_pos, T_pos


def left_move(matrix, H_pos, T_pos):
    return matrix, H_pos, T_pos


def up_move(matrix, H_pos, T_pos):
    return matrix, H_pos, T_pos


def down_move(matrix, H_pos, T_pos):
    return matrix, H_pos, T_pos


def count_visited_tiles(matrix):
    return 0


def part1(moves, matrix):
    H_pos = [len(matrix) - 1, 0]  # head position
    T_pos = [len(matrix) - 1, 0]  # tail position
    # s = [len(matrix) - 1, 0]     # start position

    for move in moves:
        if move[0] == 'R':
            matrix, H_pos, T_pos = right_move(matrix, H_pos, T_pos)
        elif move[0] == 'L':
            matrix, H_pos, T_pos = left_move(matrix, H_pos, T_pos)
        elif move[0] == 'U':
            matrix, H_pos, T_pos = up_move(matrix, H_pos, T_pos)
        elif move[0] == 'D':
            matrix, H_pos, T_pos = down_move(matrix, H_pos, T_pos)
        else:
            print("Error: unknown move")
            return -1

    return count_visited_tiles(matrix)


# ##### Main #####
moves = read_input_file()
print_moves(moves)

matrix = create_matrix()
print_matrix(matrix)

print("Solution to part 1: ", part1(moves, matrix))
