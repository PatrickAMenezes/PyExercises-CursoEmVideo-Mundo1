from unicodedata import normalize
phrase = str(input('Say something: ')).strip().lower()
normalphrase = normalize('NFD', phrase).encode('Ascii', 'ignore').decode('Ascii')
#The command normalize eliminates the accents from the phrase
print('The letter "a" appears {} times, the first time at character {}\n'
      'and the last at character {}'.format(normalphrase.count('a'), normalphrase.find('a'), 
      normalphrase.rfind('a')))
