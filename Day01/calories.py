elves = []
calories = 0

# Part 1
with open('Day01/data.txt') as file:
    for food in file:
        if food.strip():
            calories = calories + int(food)
        else:
            elves.append(calories)
            calories = 0

print(max(elves))

# Part 2
i = 0
sum = 0
while i < 3:
    sum += max(elves)
    elves.remove(max(elves))
    i = i + 1

print(sum)