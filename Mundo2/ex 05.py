age = int(input('What is the age of the athlete? '))
if age <= 9:
    print('The athlete is in the mirim category.')
elif age <= 14:
    print("The athlete is in the children's category.")
elif age <= 19:
    print("The athlete is in the junior category.")
elif age <= 25:
    print('The athlete is in the sênior category.')
else:
    print('The athlete is in the master category.')
