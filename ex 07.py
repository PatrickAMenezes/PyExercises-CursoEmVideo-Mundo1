weight = float(input('What is your weight? '))
heigth = float(input('And your height? '))
# body mass index = weight/(heigth * heigth)
bmi = weight/(heigth*heigth)
print('Your bmi is {}'.format(bmi))
if bmi < 18.5:
    print('You are underweight.')
elif bmi < 25:
    print('You are at the ideal weight.')
elif bmi < 30:
    print('You are overweight.')
elif bmi <= 40:
    print('You are obese.')
elif bmi > 40:
    print('You have morbid obesity.')
