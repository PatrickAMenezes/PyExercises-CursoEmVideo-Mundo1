num1 = int(input('Enter a number: '))
num2 = int(input('Type another number: '))
num3 = int(input('One more number: '))
if num1 > num2 > num3:
    print('The biggest number is {} and the smallest is {}'.format(num1, num3))
if num1 > num3 > num2:
    print('The biggest number is {} and the smallest is {}'.format(num1, num2))
if num2 > num1 > num3:
    print('The biggest number is {} and the smallest is {}'.format(num2, num3))
if num2 > num3 > num1:
    print('The biggest number is {} and the smallest is {}'.format(num2, num1))
if num3 > num1 > num2:
    print('The biggest number is {} and the smallest is {}'.format(num3, num2))
if num3 > num2 > num1:
    print('The biggest number is {} and the smallest is {}'.format(num3, num1))
