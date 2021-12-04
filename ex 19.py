from random import randint
num_dice = []
for p in range(0, 4):
    num_dice.append(randint(1, 6))
players_num = {'player1':num_dice[0], 'player2':num_dice[1],
             'player3':num_dice[2], 'player4':num_dice[3]}
player = []
print(f'The player1 took {players_num["player1"]}\n'
      f'The player2 took {players_num["player2"]}\n'
      f'The player3 took {players_num["player3"]}\n'
      f'The player4 took {players_num["player4"]}')
ranking = sorted(num_dice, reverse=True)
i = 1
p1 = p2 = p3 = p4 = 0
for p in ranking:
    if players_num['player1'] == p and p1 < 1:
        print(f'{i}º Place: player1 with {p}')
        p1 = 1
        i += 1
    elif players_num['player2'] == p and p2 < 1:
        print(f'{i}º Place: player2 with {p}')
        p2 = 1
        i += 1
    elif players_num['player3'] == p and p3 < 1:
        print(f'{i}º Place: player3 with {p}')
        p3 = 1
        i += 1
    elif players_num['player4'] == p and p4 < 1:
        print(f'{i}º Place: player4 with {p}')
        p4 = 1
        i += 1
