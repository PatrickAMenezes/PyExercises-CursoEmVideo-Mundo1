from datetime import date
data = {}
# Name
name = str(input('Name: ')).strip().title()
data['name'] = name
# Age
actual_year = date.today().year
birth_year = int(input('Year of birth: '))
while birth_year > actual_year:
    birth_year = int(input('Invalid date, please try again: '))
age = actual_year - birth_year
data['age'] = age
# Work Record Booklet
while True:
    wrb = int(input('Work record booklet (8 digits, absent = 0): '))
    if wrb == 0:
        break
    elif len(str(wrb)) == 8:
        break
data['wrb'] = wrb
if wrb != 0:
    # Sex
    sex = str(input('What is your sex [M/F]: ')).strip().upper()[0]
    data['sex'] = sex
    # Year of Hiring
    y_hiring = int(input('Year of hiring: '))
    while y_hiring > actual_year:
        y_hiring = int(input('Invalid date, please try again: '))
    data['y_hiring'] = y_hiring
    # Contribution Time
    contribution_t = int(input('Contribution time (years): '))
    data['contribution_t'] = contribution_t
    # Salary
    salary = int(input('Salary: R$'))
    data['salary'] = salary
    # Retirement
    if sex == 'M':
        a_retirement = 65 - age
        c_retirement = 20 - contribution_t
    elif sex == 'F':
        a_retirement = 62 - age
        c_retirement = 15 - contribution_t
    data['a_retirement'] = a_retirement
    data['c_retirement'] = c_retirement
if wrb == 0:
    print(f'The {data["name"]} have {data["age"]} years, and have no Work Record Booklet')
else:
    print(f'The {data["name"]} have {data["age"]} years and the Work Record Booklet is '
          f'{data["wrb"]}.')
    print(f'The year of hiring is {data["y_hiring"]}, the time of contribution is '
          f'{data["contribution_t"]} years, with a salary of R${data["salary"]},00.')
    if (sex == 'M' and age < 65) or (sex == 'F' and age < 62):
        print(f'To retire by age remain {data["a_retirement"]} years.')
    elif (sex == 'M' and age >= 65) or (sex == 'F' and age >= 62):
        print(f'The {data["name"]} already can retire by age.')
    if (sex == 'M' and contribution_t < 20) or (sex == 'F' and contribution_t < 15):
        print(f'To retire by contribution time remain {data["c_retirement"]} years.')
    elif (sex == 'M' and contribution_t >= 20) or (sex == 'F' and contribution_t >= 15):
        print(f'The {data["name"]} already can retire by contribution time.')
