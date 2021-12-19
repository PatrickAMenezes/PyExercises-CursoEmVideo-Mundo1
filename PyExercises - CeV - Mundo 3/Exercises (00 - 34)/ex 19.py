from random import randint
from operator import itemgetter
# Drawing numbers
players_num = {'player1':randint(1, 6), 'player2':randint(1, 6),
             'player3':randint(1, 6), 'player4':randint(1, 6)}
print('-=-'*20)
print('-- Drawn Values --\n')
for k, v in players_num.items():
    print(f'The {k} took {v}')
# Ranking of players
ranking = []
ranking = sorted(players_num.items(), key=itemgetter(1), reverse=True)
print('=-='*20)
print(f'{"":26}RANKING')
print('=-='*20)
for c, v in enumerate(ranking):
    print(f'{c+1}ºplace: {v[0]} with {v[1]}')
print('=-='*20)
