frase = 'I am learning Python'
#Fatiamento
print(frase[17])
print(frase[0:16])
print(frase[5:22:2])
print(frase[8:])
print(frase[3::2])
print(frase[:8])
print(frase[:8:2])
#Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('e', 0, 11))
print(frase.find('Pyth'))
print(frase.find('Android')) #retorna -1 quando não é encontrado
print('Py' in frase)
#Transformação
print(frase.replace('learning','suffering'))
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase.capitalize())
frase2 = '   I love Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
#Divisão
print(frase.split())
#junção
print('_'.join(frase))
