def generate_alphabet():
    a = [chr(i) for i in range(97, 123)]
    b = [chr(i) for i in range(65, 91)]
    return a + b

def wrong_item(str1, str2):
    for element in str1:
            if element in str2:
                return element

def find_badge(group):
    for element in group[0]:
        if element in group[1] and element in group[2]:
            return element


with open('Day03/items.txt') as file:
    alphabet = generate_alphabet()
    sum_p1 = 0
    sum_p2 = 0
    group = []

    for line in file:
        # remove the /n
        line = line[:-1]

        # split the line in half
        str1 = line[:len(line)//2]
        str2 = line[len(line)//2:]

        # sort the strings
        str1 = sorted(str1, key=lambda x: (x.isupper(), x))
        str2 = sorted(str2, key=lambda x: (x.isupper(), x))

        # find the wrong items        
        sum_p1 += alphabet.index(wrong_item(str1, str2)) + 1    

        # Part 2, find the badges
        group.append(line)
        if len(group) == 3:
            sum_p2 += alphabet.index(find_badge(group)) + 1
            group = []

    print("Answer 1: " + str(sum_p1))
    print("Answer 2: " + str(sum_p2))