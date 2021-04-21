from unicodedata import normalize
frase = str(input('Digite algo: ')).strip().lower()
normalfrase = normalize('NFD', frase).encode('Ascii', 'ignore').decode('Ascii')
print('A letra a aparece {} vezes, a primeira vez no caractér {}\n'
      'E a última no caractér {}'.format(normalfrase.count('a'), normalfrase.find('a'), 
      normalfrase.rfind('a')))
