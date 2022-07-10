phrase = str(input('Say a sentence: ')).strip().lower()
if phrase [0] == phrase [-1]:
    print('Is palindrome.')
else:
    print('Is not a palindrome.') 
print(phrase [0:], phrase [-0:])
