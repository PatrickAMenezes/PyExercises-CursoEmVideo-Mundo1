import coin
print('-'*45)
money = float(input('Enter the price: R$'))
print('-'*45)
print(f'The half of {coin.coin(money)} is {coin.half(money, True)}.')
print(f'The double of {coin.coin(money)} is {coin.double(money, True)}.')
print(f'Increasing 10% of {coin.coin(money)}, we have {coin.increase(money, 10, True)}.')
print(f'Decreasing 10% of {coin.coin(money)}, we have {coin.decrease(money, 10, True)}.')
print('-'*45)
print(' '*20, 'END')
print('-'*45)
