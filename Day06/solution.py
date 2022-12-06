def find_start_packet(line, check_lenght):
    stack = []
    i = 0
    for c in line:
        i += 1
        if len(stack) < check_lenght:
            stack.append(c)
            continue
        
        if(len(set(stack)) == len(stack)):
            return i
        else:
            stack.remove(stack[0])
            stack.append(c)


with open("Day06/input.txt") as file:
    print("Position for solution 1: ", find_start_packet(file.readline(), 4)-1)
    file.close()
with open("Day06/input.txt") as file:
    print("Position for solution 2: ", find_start_packet(file.readline(), 14)-1)
    file.close()