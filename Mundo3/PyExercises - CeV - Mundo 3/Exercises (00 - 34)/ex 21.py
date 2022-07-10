data_player = {}
# Player name
data_player['name'] = str(input('What is the name of the player: ')).strip().title()
# Number of matches played
while True:
    data_player['matches'] = int(input('How many matches he played?: '))
    if data_player['matches'] >= 0:
        break
# Number of goals per match
goals = []
total_goals = 0
for m in range(data_player['matches']):
    goal = int(input(f'How many goals he scored in the {m+1}º match: '))
    while True:
            if goal >= 0:
                break
            else:
                goal = int(input('Invalid number of goals, try again: '))
    goals.append(goal)
    total_goals += goal
data_player['goals'] = goals
data_player['total_goals'] = total_goals
# Player's data
print('-='*40)
print(data_player)
print('-='*40)
print(f'The player {data_player["name"]} played {data_player["matches"]} matches.')
for m in range(len(data_player['goals'])):
    if data_player["goals"][m] == 0:
        print(f'In the {m+1}º match, he didn\'t make goal.')
    elif data_player["goals"][m] == 1:
        print(f'In the {m+1}º match, did {data_player["goals"][m]} goal.')
    else:
        print(f'In the {m+1}º match, did {data_player["goals"][m]} goals.')
print(f'The total of goals was {data_player["total_goals"]}.')
print('-='*40)
