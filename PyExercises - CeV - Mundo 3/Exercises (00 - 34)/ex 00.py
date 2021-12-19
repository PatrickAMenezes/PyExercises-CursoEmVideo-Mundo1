count = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eigth', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fithteen', 'sixteen', 'seventeen',
         'eighteen', 'nineteen', 'twenty')
while True:
    num = int(input('Insert a number between 0 and 20: '))
    while num < 0 or num > 20:
            num = int(input('Try again. Please insert a number between 0 and 20: '))
    if 0 <= num <= 20:
        print(f'Your typed the number {count[num]}.')
        break
