def player_data(p_name=0, p_goals=0):
    print('-'*57)
    p_name = str(input('What is the player name?: ')).strip().title()
    p_goals = str(input('How many goals he did?[numeric]: ')).strip()
    if p_name == '':
        p_name = '<unknown>'
    if p_goals == '' or p_goals.isnumeric() == False:
        p_goals = 0
    print(f'The player {p_name} scored {p_goals} goal(s) in the championship.')
    print('-'*57)


player_data()
