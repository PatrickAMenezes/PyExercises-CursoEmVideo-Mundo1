goals = []
players = []
player_data = {}
while True:
    player_name = str(input('Insert the player name: ')).strip().title()
    player_data['player_name'] = player_name
    matches = int(input('How many matches he played?: '))
    total_goals = 0
    for m in range(matches):
        goal = int(input(f'How many goals he did in the {m+1}º match?: '))
        goals.append(goal)
        total_goals += goal
    player_data['goals'] = goals[:]
    goals.clear()
    player_data['total_goals'] = total_goals
    players.append(player_data.copy())
    cont = str(input('Do you want to continue?[y/n]: ')).strip().lower()[0]
    while cont not in 'yn':
        cont = str(input('Do you want to continue?[y/n]: ')).strip().lower()[0]
    if cont == 'n':
        break
print('=-='*20)
print(f'Cod{"":4}Player{"":15}Goals{"":15}Total')
print('-'*60)
for c in range(len(players)):
    print(f'{c+1}{"":6}{players[c]["player_name"]:21}{str(players[c]["goals"]):22}{players[c]["total_goals"]}')
print('-'*60)
while True:
    show = int(input('Which player data do you want to see [0 to stop]: '))
    if show == 0:
        break
    elif show > len(players) or show < 0:
        print('There\'s no player with that code.')
    else:
        for c in range(len(players)):
            if show == c+1:
                print(f'----- DATA OF {str(players[c]["player_name"]).upper()} -----')
                for m in range(len(players[c]['goals'])):
                    print(f'In the {m+1}º game did {players[c]["goals"][m]} goals')
    print('-'*60)
print('=-='*20)
print(' '*26 + 'FINISHED' + ' '*26)
print('=-='*20)
