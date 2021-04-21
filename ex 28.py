dist = int(input('Qual é a distância da viagem, em km: '))
print('Sua viagem será de {}km.'.format(dist))
if dist <= 200:
    preço = dist*0.50
else:
    preço = dist*0.45
print('O valor da passagem será de R${:.2f}.'.format(preço))
