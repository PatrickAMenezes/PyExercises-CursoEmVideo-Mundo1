daysr = int(input('How many days rented: '))
kmrun = int(input('How many kilometers run: '))
amount = (daysr*60) + (kmrun*0.15)
print('The amount to pay, considering that the car was rented\n'
      'for a total of {}days and traveled {}km, is R${:.2f}'.format(daysr, kmrun, amount))
