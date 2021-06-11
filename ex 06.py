segment1 = float(input('Length of the first segment: '))
segment2 = float(input('Length of the second segment: '))
segment3 = float(input('Length of the third segment: '))
case1 = segment1 < segment2 + segment3
case2 = segment2 < segment1 + segment3
case3 = segment3 < segment1 + segment2
case4 = segment1 == segment2 != segment3
case5 = segment1 == segment3 != segment2
case6 = segment2 == segment3 != segment1
istriangle = case1 and case2 and case3
if istriangle:
    print('The segments form a triangle.')
if segment1 == segment2 == segment3 and istriangle:
    print('The triangle is equilateral.')
elif case4 or case5 or case6 and istriangle:
    print('The triangle is isosceles.')
elif segment1 != segment2 != segment3 and istriangle:
    print('The triangle is scalene.')
else:
    print('The segments do not form a triangle.')
