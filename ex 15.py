from random import choice
s1 = str(input('The name of the first student: '))
s2 = str(input('The second: '))
s3 = str(input('The third: '))
s4 = str(input('The fourth: '))
students = [s1, s2, s3, s4]
chosen = choice(students)
print('The student chosen to erase the board is {}'.format(chosen))
