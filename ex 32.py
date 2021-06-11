line1 = float(input('Length of segment 1: '))
line2 = float(input('Length of segment 2: '))
line3 = float(input('Length of segment 3: '))
case1 = line3 < line1 + line2 
case2 = line2 < line1 + line3
case3 = line1 < line2 + line3
if case1 and case2 and case3:
    print('The segments form a triangle')
else:
    print("The segments don't form a triangle")
