from math import hypot
catop = float(input('Dê o valor do cateto oposto: '))
catadj = float(input('Dê o valor do cateto adjacente: '))
hipo = hypot(catadj, catop)
print('A hipotenusa do triângulo cujo cateto adjacente vale {:.2f} \n'
      'e o cateto oposto vale {:.2f}, vale {:.2f}'.format(catadj, catop, hipo))
