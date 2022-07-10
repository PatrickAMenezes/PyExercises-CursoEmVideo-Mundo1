from datetime import date
yearborn = int(input('Type the year that you born: '))
now = date.today().year
age = now - yearborn
timepassed = abs(age - 18)
print('So, you have {} years old in {}.'.format(age, now))
if age == 18:
    print('You need to enlist in the army.')
elif age < 18:
    print('You are not 18 years old, {} years left to you enlist in the army, that will be in {}.'
          .format(timepassed, timepassed + now))
elif age > 18:
    print('You are older than 18, passed {} years of the enlistment that had to be in {}.'
          .format(timepassed, now - timepassed))
