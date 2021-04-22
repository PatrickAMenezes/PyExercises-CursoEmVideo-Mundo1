import math
angle = int(input('Give any angle: '))
anglerad = math.radians(angle)
cos = math.cos(anglerad)
sin = math.sin(anglerad)
tan = math.tan(anglerad)
print('The sine, cossino and tangent of {}° are, respectively, {:.2f}, {:.2f} and {:.2f}'
      .format(angle, sin, cos, tan))
