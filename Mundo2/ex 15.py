first_term = int(input('Insert the first term of an arithmetic progression: '))
reason = int(input('Insert the reason of the arithmetic progression: '))
for c in range (1, 11):
    if reason == 0:
        print(first_term)
    elif reason > 0:
        c = first_term + (c - 1)*reason
        print(c)
    else:
        c = first_term + (c - 1)*reason
        print(c)
# first_term + (c - 1)*reason is the general term formula of the arithmetic progression
