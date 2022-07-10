spd = int(input('Which is the speed of the car in km/h: '))
if spd > 80:
    print('You crossed the speed limit, your traffic ticket is of R${:.2f}'
          .format((spd - 80)*7))
else:
    print('You is in the speed limit, good travel :)')
