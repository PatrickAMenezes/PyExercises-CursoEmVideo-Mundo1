def write(phrase):
    size = len(str(phrase)) + 4
    print('-'*size)
    print(' '*2 + phrase)
    print('-'*size)


phrase = str(input('Type a phrase: ')).strip()
write(phrase)
