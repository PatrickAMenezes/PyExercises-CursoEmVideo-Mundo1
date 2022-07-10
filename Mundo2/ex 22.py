from random import randint
robot = randint(0, 10)
user = int(input('Try to guess which number I\'m thinking: '))
counter = 0
while robot != user:
    counter += 1
    print('Missed!')
    if robot > user:
        user = int(input('Is greater, try again: '))
    elif robot < user:
        user = (int(input('Is smaller, try again: ')))
print('Congratulations, you got it after {} attempts.'.format(counter + 1))
