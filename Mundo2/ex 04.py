note1 = float(input('The first note of the student: '))
note2 = float(input('The second note of the student: '))
average = (note1 + note2)/2
if average < 5.0:
    print('The student was reproved')
elif average <=6.9:
    print('The student is in recovery')
else:
    print('The student has been approved')
