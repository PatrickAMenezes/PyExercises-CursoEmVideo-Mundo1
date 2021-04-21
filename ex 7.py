larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = (alt*larg)
print('A quantidade de tinta necessária pra pintar a parede, que mede {}x{},\n'
      'e cuja área é de {}m² é {:.2f}l'
      .format(larg, alt, area, area/2))
