phrase = 'I am learning Python'
#Slicing
print(phrase[17])
print(phrase[0:16])
print(phrase[5:22:2])
print(phrase[8:])
print(phrase[3::2])
print(phrase[:8])
print(phrase[:8:2])
#Analysis
print(len(phrase))
print(phrase.count('o'))
print(phrase.count('e', 0, 11))
print(phrase.find('Pyth'))
print(phrase.find('Android')) #retorna -1 quando não é encontrado
print('Py' in phrase)
#Transformation
print(phrase.replace('learning','suffering'))
print(phrase.upper())
print(phrase.lower())
print(phrase.title())
print(phrase.capitalize())
phrase2 = '   I love Python  '
print(phrase2.strip())
print(phrase2.rstrip())
print(phrase2.lstrip())
#Division
print(phrase.split())
#junction
print('_'.join(phrase))
