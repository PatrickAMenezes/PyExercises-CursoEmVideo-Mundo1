from datetime import date
actual_year = date.today().year
def vote(yb):
    age = actual_year - yb
    if age >= 70 or (16 <= age < 18):
        print('The vote is optional.')
    elif age < 16:
        print('The vote is denied.')
    else:
        print('The vote is mandatory.')


year_birth = int(input('Insert the year of birth: '))
while year_birth > actual_year:
    year_birth = int(input('Invalid date, insert a correct birth year: '))
vote(year_birth)
