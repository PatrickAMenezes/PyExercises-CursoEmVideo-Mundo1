s = c = 0
while True:
    num = int(input('Insert a number [999 to stop]: '))
    if num == 999:
        break
    s += num
    c += 1
print(f'You inserted a total of {c} numbers whose sum is {s}.')
