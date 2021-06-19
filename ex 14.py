s = 0 # s = sum
for c in range(1, 7):
    num = int(input('Insert a number: '))
    if num%2 == 0:
        s += num
print(s)
