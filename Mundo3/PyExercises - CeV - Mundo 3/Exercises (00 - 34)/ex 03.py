num = (int(input('Insert a number: ')), int(input('Another number: ')),
       int(input('Other one: ')), int(input('One more number: ')))
print(f'You inputed the numbers: {num}.')
print(f'The number 9 appears {num.count(9)} times.')
if 3 in num:
    print(f'The number 3 appears for the first time in the {num.index(3)+1}° position')
print('The par numbers typeds is ', end='')
for n in num: 
    if n % 2 == 0:
        print(n, end=' ')
