teams = ('Bragantino', 'Athletico-PR', 'Palmeiras', 'Fortaleza', 'Santos', 'Juventude',
         'Bahia', 'Atlético-GO', 'Atlético-MG', 'Corinthians', 'Fluminense', 'Flamengo',
         'Ceará-SC', 'Internacional', 'Sport Recife', 'América-MG', 'São Paulo', 'Cuiabá',
         'Chapecoense', 'Grêmio')
print(f'List of Brazilian Soccer Championship teams: {teams}')
print('~'*140)
print(f'The 5 first placed teams: {teams[0:5]}')
print('~'*140)
print(f'The 4 last placed teams: {teams[-4:]}')
print('~'*140)
print(f'Teams in alphabetic order: {sorted(teams)}')
print('~'*140)
print('The team Chapecoense is in the {}° position of the Brazilian Soccer Championship.'
      .format(teams.index('Chapecoense') + 1))
