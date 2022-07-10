width = float(input('Wall width: '))
hight = float(input('Wall hight: '))
area = (hight*width)
print('The quantity of ink necessary to paint the wall, that measures {}x{},\n'
      'and whose area is {}m² is {:.2f}l'
      .format(width, hight, area, area/2))
