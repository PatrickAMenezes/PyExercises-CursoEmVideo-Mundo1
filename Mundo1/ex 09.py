sal = float(input('Type the salary of the functionary: '))
inc = (sal*15)/100
newsal = sal + inc
print('The new salary of the employee, with a 15% increase, is R${:.2f}'.format(newsal))
