from math import sqrt
# write a function that returns the euclidean distance between two points
def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


with open('Day09/input.txt') as file:
    moves = []
    for line in file:
        moves.append(line.strip().split(' '))
    for element in moves:
        print(element)

    #        X  Y 
    H_pos = [0, 0]
    T_pos = [0, 0]
    visited_pos = []          # positions visited by the tail
    visited_pos.append(T_pos.copy()) # add starting position
    for move in moves:
        for i in range(int(move[1])):
            
            if H_pos == T_pos: # head and tail same position
                if move[0] == 'R':
                    H_pos[0] += 1
                elif move[0] == 'L':
                    H_pos[0] -= 1
                elif move[0] == 'U':
                    H_pos[1] += 1
                elif move[0] == 'D':
                    H_pos[1] -= 1
                continue

            if move[0] == 'R':
                if distance(T_pos[0], T_pos[1], H_pos[0] + 1, H_pos[1]) < 1.5:
                    H_pos[0] += 1
                    continue
                if T_pos[1] == H_pos[1]:     # if same y 
                    T_pos[0] += 1            # add to x
                else:                        # if not same y
                    T_pos = H_pos.copy()      # diagonal movement
                H_pos[0] += 1                # move head

            elif move[0] == 'L':
                if distance(T_pos[0], T_pos[1], H_pos[0] - 1, H_pos[1]) < 1.5:
                    H_pos[0] -= 1
                    continue
                if T_pos[1] == H_pos[1]:
                    T_pos[0] -= 1
                else:
                    T_pos = H_pos.copy()
                H_pos[0] -= 1

            elif move[0] == 'U':
                if distance(T_pos[0], T_pos[1], H_pos[0], H_pos[1] + 1) < 1.5:
                    H_pos[1] += 1
                    continue
                if T_pos[0] == H_pos[0]:     # if same x
                    T_pos[1] += 1            # add to y
                else:                        # if not same x
                    T_pos = H_pos.copy()      # diagonal movement
                H_pos[1] += 1                # move head

            elif move[0] == 'D':
                if distance(T_pos[0], T_pos[1], H_pos[0], H_pos[1] - 1) < 1.5:
                    H_pos[1] -= 1
                    continue
                if T_pos[0] == H_pos[0]:
                    T_pos[1] -= 1
                else:
                    T_pos = H_pos.copy()
                H_pos[1] -= 1
            
            if T_pos not in visited_pos: 
                visited_pos.append(T_pos.copy())
    

    print("Solution to part 1: ", len(visited_pos))
    file.close()