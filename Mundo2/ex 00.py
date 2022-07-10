house = float(input('Insert the value of the house: R$'))
salary = float(input('Buyer salary: R$'))
years_to_pay = int(input('How many years it will pay: '))
months = years_to_pay*12 # Converting years to months
installments = house/months
print('To afford a house of R${:.2f} in {} years the\n installment'
      'will be R${:.2f}'.format(house, years_to_pay, installments))
if installments*100/salary <= 30:
    print('You can afford the house.')
else:
    print("You can't afford the house.")
