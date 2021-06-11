from datetime import datetime
yearborn = int(input('Type the year that you born: '))
now = datetime.now()
birthdate = now.year - yearborn
timepassed = abs(birthdate - 18)
print('So, you have {} years old in {}.'.format(birthdate, now.year))
if birthdate == 18:
    print('You need to enlist in the army.')
elif birthdate < 18:
    print('You are not 18 years old, {} years left to you enlist in the army, that will be in {}.'
          .format(timepassed, timepassed + now.year))
elif birthdate > 18:
    print('You are older than 18, passed {} years of the enlistment that had to be in {}.'
          .format(timepassed, now.year - timepassed))
