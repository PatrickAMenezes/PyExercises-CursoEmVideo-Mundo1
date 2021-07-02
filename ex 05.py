words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for w in words:
    print(f'\nThe vowels in the word {w} are: ', end='')
    for vowels in w:
        if vowels in 'aeiou':
                print(vowels, end='')
