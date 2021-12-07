goals = []
players = []
player_data = {}
# Registering the player's data
while True:
    # The player's name and the number of matches played.
    player_data['player_name'] = str(input('Insert the player name: ')).strip().title()
    while True:
        matches = int(input('How many matches he played?: '))
        if matches >= 0:
            break
    total_goals = 0
    # The quantity of goals that he did.
    for m in range(matches):
        goal = int(input(f'How many goals he did in the {m+1}º match?: '))
        while True:
            if goal >= 0:
                break
            else:
                goal = int(input('Invalid number of goals, try again: '))
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
# Showing The list of players
print('=-='*20)
print(f'Cod{"":4}Player{"":15}Goals{"":15}Total')
print('-'*60)
for c in range(len(players)):
    if len(players[c]['goals']) == 0:
        print(f'{c+1}{"":6}{players[c]["player_name"]}: didn\'t play any match.')
    else:
        print(f'{c+1}{"":6}{players[c]["player_name"]:21}{str(players[c]["goals"]):22}{players[c]["total_goals"]}')
print('-'*60)
# Player data analysis
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
                if len(players[c]['goals']) == 0:
                    print(f'He didn\'t play any match.')
                else:
                    for m in range(len(players[c]['goals'])):
                        if players[c]["goals"][m] == 0:
                            print(f'In the {m+1}º game, he didn\'t make goal.')
                        elif players[c]["goals"][m] == 1:
                            print(f'In the {m+1}º game, did {players[c]["goals"][m]} goal.')
                        else:
                            print(f'In the {m+1}º game, did {players[c]["goals"][m]} goals')
    print('-'*60)
print('=-='*20)
print(' '*26 + 'FINISHED' + ' '*26)
print('=-='*20)
