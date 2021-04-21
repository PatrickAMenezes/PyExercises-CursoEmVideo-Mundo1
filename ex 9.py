sal = float(input('Digite o salário do funcionário: '))
aum = (sal*15)/100
novsal = sal + aum
print('O novo salário do funcionário, com 15% de aumento, é R${:.2f}'.format(novsal))
