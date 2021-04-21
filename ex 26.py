vel = int(input('Qual é a velocidade do carro em km/h: '))
if vel > 80:
    print('Você ultrapassou o limite de velocidade, sua multa é de R${:.2f}'
          .format((vel - 80)*7))
else:
    print('Você está no limite de velocidade, boa viajem :)')
