x = int(input('Type a number: '))
contour = '|'
print('The times table of {} is: '.format(x))
print('-'*19)
print('| {:2}  x   1 = {:>2} {:>2}'.format(x, x, contour))
print('| {:2}  x   2 = {} {:>2}'.format(x, x*2, contour))
print('| {:2}  x   3 = {} {:>2}'.format(x, x*3, contour))
print('| {:2}  x   4 = {} {:>2}'.format(x, x*4, contour))
print('| {:2}  x   5 = {} {:>2}'.format(x, x*5, contour))
print('| {:2}  x   6 = {} {:>2}'.format(x, x*6, contour))
print('| {:2}  x   7 = {} {:>2}'.format(x, x*7, contour))
print('| {:2}  x   8 = {} {:>2}'.format(x, x*8, contour))
print('| {:2}  x   9 = {} {:>2}'.format(x, x*9, contour))
print('| {:2}  x  10 = {}  {}'.format(x, x*10, contour))
print('-'*19)