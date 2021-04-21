reta1 = float(input('Comprimento da reta 1: '))
reta2 = float(input('Comprimento da reta 2: '))
reta3 = float(input('Comprimento da reta 3: '))
caso1 = reta3 < reta1 + reta2 
caso2 = reta2 < reta1 + reta3
caso3 = reta1 < reta2 + reta3
if caso1 and caso2 and caso3:
    print('As três retas formam um triângulo')
else:
    print('As três retas não formam um triângulo')
