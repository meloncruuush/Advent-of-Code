strategy_guide = []

# Part 1
with open('Day02/input.txt') as file:
    for line in file:
        strategy_guide.append((line[0], line[2]))

score = 0
for round in strategy_guide:
    # increase the score based on the shape
    if round[1] == 'X':
        score += 1
    if round[1] == 'Y':                     # A: rock, B: paper, C: scissors
        score += 2                          # X: rock, Y: paper, Z: scissors
    if round[1] == 'Z':
        score += 3
    
    # play the round
    if (round[0] == 'A' and round[1] == 'X') or (round[0] == 'B' and round[1] == 'Y') or (round[0] == 'C' and round[1] == 'Z') : # Draw     
        score += 3                  
    elif round[0] == 'C' and round[1] == 'X': # rock defeats scissors 
        score += 6 
    elif round[0] == 'B' and round[1] == 'Z': # scissors defeats paper 
        score += 6
    elif round[0] == 'A' and round[1] == 'Y': # paper defeats rock
        score += 6
    else: # I lose the round
        pass

print("First answer: " + str(score))


# second part
score = 0
for round in strategy_guide: # X: lose, Y: draw, Z: win    
    if round[1] == 'X': # lose the round
        if round[0] == 'A': 
            player2_hand = 'scissors'
        if round[0] == 'B':
            player2_hand = 'rock'
        if round[0] == 'C':
            player2_hand = 'paper'                                       

    if round[1] == 'Y': # draw the round            # A: rock, B: paper, C: scissors
        if round[0] == 'A':                         # X: rock, Y: paper, Z: scissors
            player2_hand = 'rock'
        if round[0] == 'B':
            player2_hand = 'paper'
        if round[0] == 'C':
            player2_hand = 'scissors'   
        score += 3                                     

    if round[1] == 'Z': # win the round
        if round[0] == 'A':
            player2_hand = 'paper'
        if round[0] == 'B':
            player2_hand = 'scissors'
        if round[0] == 'C':
            player2_hand = 'rock'
        score += 6

    # increase the score based on the shape
    if player2_hand == 'rock':
        score += 1
    if player2_hand == 'paper':                     
        score += 2                          
    if player2_hand == 'scissors':
        score += 3
    
print("Second answer: " + str(score))
