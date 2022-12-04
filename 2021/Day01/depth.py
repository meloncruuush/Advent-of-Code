with open("2021/Day01/depths.txt", "r") as file:
    
    first_measurement = True
    sum = 0
    
    for line in file:
        if first_measurement:
            first_measurement = False
            previous = line
            continue

        if line > previous:
            sum += 1

        previous = line
        
    print(sum)