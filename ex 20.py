from datetime import date
data = {}
# Name
data['name'] =  str(input('Name: ')).strip().title()
# Age
actual_year = date.today().year
birth_year = int(input('Year of birth: '))
while birth_year > actual_year:
    birth_year = int(input('Invalid date, please try again: '))
age = actual_year - birth_year
data['age'] = age
# Work Record Booklet
while True:
    data['wrb'] = int(input('Work record booklet (8 digits, absent = 0): '))
    if data['wrb'] == 0:
        break
    elif len(str(data['wrb'])) == 8:
        break
if data['wrb'] != 0:
    # Sex
    sex = str(input('What is your sex [M/F]: ')).strip().upper()[0]
    data['sex'] = sex
    # Year of Hiring
    data['y_hiring'] = int(input('Year of hiring: '))
    while data['y_hiring'] > actual_year:
        data['y_hiring'] = int(input('Invalid date, please try again: '))
    # Contribution Time
    contribution_t = int(input('Contribution time (years): '))
    data['contribution_t'] = contribution_t
    # Salary
    data['salary'] = int(input('Salary: R$'))
    # Retirement
    if sex == 'M':
        data['a_retirement'] = 65 - age
        data['c_retirement'] = 20 - contribution_t
    elif sex == 'F':
        data['a_retirement'] = 62 - age
        data['c_retirement'] = 15 - contribution_t
print('=-='*40)
if data['wrb'] == 0:
    print(f'The {data["name"]} have {age} years, and have no Work Record Booklet')
else:
    print(f'The {data["name"]} have {age} years and the Work Record Booklet is '
          f'{data["wrb"]}.')
    print(f'The year of hiring is {data["y_hiring"]}, the time of contribution is '
          f'{data["contribution_t"]} years, with a salary of R${data["salary"]},00.')
    if (sex == 'M' and age < 65) or (sex == 'F' and age < 62):
        print(f'To retire, remain {data["a_retirement"]} years.')
    elif (sex == 'M' and age >= 65) or (sex == 'F' and age >= 62):
        print(f'The {data["name"]} already can retire.')
    if (sex == 'M' and contribution_t < 20) or (sex == 'F' and contribution_t < 15):
        print(f'You need to contribute {data["c_retirement"]} more years.')
    elif (sex == 'M' and contribution_t >= 20) or (sex == 'F' and contribution_t >= 15):
        print(f'You already contributed for {contribution_t} years.')
print('=-='*40)
