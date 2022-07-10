value = float(input('Input the value to be paid: R$'))
print('Cash or check (1), card in cash (2), twice times in the card (3), thrice or more times in the card (4)')
payment = int(input('Form of payment: '))
if payment ==4:
    installment = int(input('Number of installments: '))
# percentage(discount): money - percentage*money
cash_check = abs(value - 10*value/100)
card_in_cash = abs(value - 5*value/100)
# percentage(increase): money + percentage*money
card3x = value + 20*value/100
if payment == 1:
    print('Your payment will be with cash/check. The value, with a discount of 10%, is R${:.2f}.'.format(cash_check))
elif payment == 2:
    print('Your payment will be with the card in installment. The value, with a discount of 5%, is R${:.2f}.'.format    (card_in_cash))
elif payment == 3:
    print('Your payment will be twice times on the card. The value has no modification, you have to pay R${:.2f}.'.format(value))
elif payment == 4:
    print('Your payment will be in {} times. The value, with interest of 20%, is R${:.2f}\n'
    'and the installment will be of R${:.2f}'.format(installment, card3x, card3x/installment))
else:
    print('Please, select one of the options listed.')
