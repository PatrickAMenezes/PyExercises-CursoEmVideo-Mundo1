data_player = {}
# Player name
name = str(input('What is the name of the player: ')).strip().title()
data_player['name'] = name
# Number of matches played
matches = int(input('How many matches he played: '))
data_player['matches'] = matches
# Number of goals per match
goals = []
total_goals = 0
for m in range(matches):
    goal = int(input(f'How many goals he scored in the {m+1}º match: '))
    goals.append(goal)
    total_goals += goal
data_player['goals'] = goals
data_player['total_goals'] = total_goals
print('-='*40)
print(data_player)
print('-='*40)
print(f'The player {data_player["name"]} played {data_player["matches"]} matches.')
for m in range(len(data_player['goals'])):
    print(f'In the {m+1}º match, did {data_player["goals"][m]} goals')
print(f'The total of goals was {data_player["total_goals"]}.')
print('-='*40)
