withdraw = int(input('Insert how much money do you want to withdraw: R$'))
total = withdraw
c = 0
notes = 50
while True:
    if total >= notes:
        total -= notes
        c += 1
    else:
        if c > 0:
            print(f'Total of {c} notes of R${notes},00')
        if notes == 50:
            notes = 20
        elif notes == 20:
            notes = 10
        elif notes == 10:
            notes = 1
        c = 0
        if total == 0:
            break
print('----------- END ----------')
