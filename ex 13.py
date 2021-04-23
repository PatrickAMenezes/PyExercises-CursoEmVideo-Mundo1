from math import hypot
sin = float(input('The value of the sine: '))
cos = float(input('The value of the cosine: '))
hypot = hypot(sin, cos)
print('The hypotenuse of the triangle, whose opposite leg worth {:.2f} \n'
      'and the adjacent leg worth {:.2f}, is {:.2f}'.format(sin, cos, hypot))
