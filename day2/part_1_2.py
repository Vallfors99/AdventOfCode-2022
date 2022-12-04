input_file = 'day2\input.txt'
with open(input_file) as infile:
    rounds = [line.strip('\n') for line in infile]
    rounds = [play.split(' ') for play in rounds]


value_of_play = {'A': 1, 'B':2, 'C':3, 'X':1, 'Y':2,'Z':3}
wins_player = [['A','Y'],['B','Z'],['C','X']]
opponent_scores = []
player_scores = []

for round in rounds:
    if value_of_play[round[0]] == value_of_play[round[1]]: #draw
        opponent_scores.append(3 + value_of_play[round[0]])
        player_scores.append(3 + value_of_play[round[1]])

    elif round in wins_player: #player won
        opponent_scores.append(0 + value_of_play[round[0]])
        player_scores.append(6 + value_of_play[round[1]])

    else: # opponent won
        opponent_scores.append(6 + value_of_play[round[0]])
        player_scores.append(0 + value_of_play[round[1]])
    
print(sum(player_scores))

# part 2
list_plays = ['A','B','C']
score_total = 0
for round in rounds:
    idx_opponent_play  = list_plays.index(round[0])
    if round[1] == 'X': # loose
        score_round = 0
        player_play = list_plays[(idx_opponent_play - 1) % len(list_plays)] # player plays previous value in order
    elif round[1] == 'Y': # tie
        player_play = round[0]
        score_round = 3
    else: 
        player_play = list_plays[(idx_opponent_play + 1) % len(list_plays)] # player plays next value in order
        score_round = 6
    score_total += score_round + value_of_play[player_play]
print(score_total)
