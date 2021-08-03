student = list()
classroom = list()
print('-=-'*30)
while True:
    name = str(input('Insert the name of the student: ')).strip().title()
    grade1 = float(input('The first grade: '))
    grade2 = float(input('The second grade: '))
    avg = (grade1 + grade2)/2
    student.append([name, grade1, grade2, [avg]])
    cont = str(input('Do you want to insert more students? [y/n]: ')).strip().lower()[0]
    while cont not in 'yn':
        cont = str(input('Do you want to insert more students? [y/n]: ')).strip().lower()[0]
    if cont == 'n':
        break
print('-'*30)
for i in range(len(student)):
    print(f'Student: {student[i][0]}')
    print(f'1° grade: {student[i][1]}')
    print(f'2° grade: {student[i][2]}')
    print(f'Average: {student[i][3]}')
    print('-'*30)
confirmation = ''
while True:
    show = str(input('Do you want to show the grade of a student in specific? [y/n]: ')
    ).strip().lower()[0]
    while show not in 'yn':
        show = str(input('Do you want to show the grade of a student in specific? [y/n]: ')
        ).strip().lower()[0]
    if show == 'n':
        break
    selection = str(input('Which: ')).strip().title()
    for i in range(len(student)):
        if selection in student[i]:
            print('-'*30)
            print(f'Student: {student[i][0]}')
            print(f'1° grade: {student[i][1]}')
            print(f'2° grade: {student[i][2]}')
            print(f'Average: {student[i][3]}')
            print('-'*30)
            confirmation = 'yes'
        if i == len(student):
            if selection not in student[i]:
                confirmation == 'no'
    if confirmation == 'yes':
        cont = str(input('Do you want to show another one? [y/n]: ')).strip().lower()[0]
        while cont not in 'yn':
            cont = str(input('Do you want to show another one? [y/n]: ')).strip().lower()[0]
        while cont == 'y':
            confirmation = ''
            selection = str(input('Which: ')).strip().title()
            for i in range(len(student)):
                if selection in student[i]:
                    print('-'*30)
                    print(f'Student: {student[i][0]}')
                    print(f'1° grade: {student[i][1]}')
                    print(f'2° grade: {student[i][2]}')
                    print(f'Average: {student[i][3]}')
                    print('-'*30)
                    confirmation = 'yes'
                if i == len(student):
                    if selection not in student[i]:
                        confirmation = 'no'
            if confirmation == 'yes':
                cont = str(input('Do you want to show another one? [y/n]: ')).strip().lower()[0]
                while cont not in 'yn':
                    cont = str(input('Do you want to show another one? [y/n]: ')).strip().lower()
            else:
                print('There\'s no student with this name.')
        if cont == 'n':
            break
    else:
        print('There\'s no student with this name.')
print('-=-'*30)
