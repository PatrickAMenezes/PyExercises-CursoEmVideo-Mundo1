year = int(input('Type the year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year is {} is leap'.format(year))
else:
    print('The year {} is not leap'.format(year))
