sal = float(input('Qual é o salário do funcionário? '))
if sal > 1250.00:
    print('O salário, com o aumento, passou a ser de R${:.2f}'
          .format((sal*10)/100 + sal))
else:
    print('O salário, com o aumento, passou a ser de R${:.2f}'
          .format((sal*15)/100 + sal))
