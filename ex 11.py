dalug = int(input('Quantos dias alugador: '))
kmrod = int(input('Quantos km rodados: '))
valtotal = (dalug*60) + (kmrod*0.15)
print('O total a pagar, levando em conta que o carro foi alugado\n'
      'por um total de {}dias e rodou {}km, é de R${:.2f}'.format(dalug, kmrod, valtotal))
