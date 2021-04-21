import math
ang = int(input('Dê um ângulo qualquer: '))
angrad = math.radians(ang)
cos = math.cos(angdeg)
sen = math.sin(angdeg)
tan = math.tan(angdeg)
print('O seno, cosseno e tangente de {}° são, respectivamente, {:.2f}, {:.2f} e {:.2f}'
      .format(ang, sen, cos, tan))
