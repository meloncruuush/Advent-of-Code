def perimeter(forest):
    height = len(forest)
    base = len(forest[0])
    perimeter = 2 * (height + base) - 4
    return perimeter


def is_visible(forest, line, column):
    # Right
    j = column + 1
    visible = True
    while j < len(forest[line]):
        if forest[line][column] <= forest[line][j]:
            visible = False
            break
        j += 1
    if visible:
        return True
    
    # Left
    j = column - 1
    visible = True
    while j >= 0:
        if forest[line][column] <= forest[line][j]:
            visible = False
            break
        j -= 1
    if visible:
        return True

    # Up
    i = line - 1
    visible = True
    while i >= 0:
        if forest[line][column] <= forest[i][column]:
            visible = False
            break
        i -= 1
    if visible:
        return True

    # Down
    i = line + 1
    visible = True
    while i < len(forest):
        if forest[line][column] <= forest[i][column]:
            visible = False
            break
        i += 1
    if visible:
        return True
    
    return False


def count_visible_trees(forest):
    visible_trees = 0
    i = 1
    while i < len(forest) - 1:
        j = 1
        while j < len(forest[i]) - 1:
            if is_visible(forest, i, j):
                visible_trees += 1
            j += 1
        i += 1
    return visible_trees


# ############################## MAIN ##############################
forest = []
with open('Day08/input.txt') as file:
    for line in file:
        row = []
        for charater in line:
            if charater != '\n':
                row.append(charater.strip())
        forest.append(row)


visible_trees = perimeter(forest)
visible_trees += count_visible_trees(forest)
print("Answer 1: ", visible_trees)