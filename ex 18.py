# Student name
print('What is the student\'s name?')
name = str(input('Name: ')).title().strip()
# Grades
print(f'What is the first grade of {name}?')
grade1 = int(input('Grade (1): '))
while grade1 > 10 or grade1 < 0:
    grade1 = int(input('Invalid, try again (grade 1): '))
print(f'What is the secong grade of {name}?')
grade2 = int(input('Grade (2): '))
while grade2 > 10 or grade2 < 0:
    grade2 = int(input('Invalid, try again (grade 2): '))
# Average
avg = (grade1 + grade2)/2
student = {'name':name, 'average':avg}
print(f'The average of {student["name"]} is {student["average"]}')
print('-'*20)
# Student situation
if student['average'] >= 6:
    print('Situation: Approved!')
else:
    print('Situation: disapproved!')
print('-'*20)
