first_term = int(input('Insert the first term of an Arithmetic Progression: '))
reason = int(input('Insert the reason of the arithmetic progression: '))
c = False
n = 0
while not c:
    ap = first_term + reason*n
    print(ap)
    if n == 9:
        c = True
    else:
        n += 1
