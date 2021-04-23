dist = int(input('How far is the trip, in km: '))
print('Your travel will be of {}km.'.format(dist))
if dist <= 200:
    price = dist*0.50
else:
    price = dist*0.45
print('The value of the ticket will be of R${:.2f}.'.format(price))
