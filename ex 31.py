sal = float(input("What is the employee's salary? "))
if sal > 1250.00:
    print('The salary, with increase, passed to be of R${:.2f}'
          .format((sal*10)/100 + sal))
else:
    print('The salary, with increase, passed to be of R${:.2f}'
          .format((sal*15)/100 + sal))
