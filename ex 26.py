from time import sleep
def count1():
    print('-='*20)
    print('Counting from 1 to 10 of 1 in 1:')
    for c in range (1, 10+1):
        print(c, end=' ', flush=True)
        sleep(0.3)
    print('END!')
    print('-='*20)


def count2():
    print('-='*20)
    print('Counting from 10 to 0 of 2 in 2:')
    for c in range(10, -1, -2):
        print(c, end=' ', flush=True)
        sleep(0.3)
    print('END!')
    print('-='*20)


def count3():
    print('-='*20)
    print('Now it\'s your turn.')
    start = int(input('Start: '))
    end = int(input('End: '))
    step = int(input('Step: '))
    print('-='*20)
    print(f'Counting from {start} to {end} of {step} in {step}:')
    if step == 0:
        step = 1
    if end < start and step > 0:
        step *= -1
        end -= 1
    elif end < start and step < 0:
        end -= 1
    elif start < end:
        end += 1
    for c in range(start, end, step):
        print(c, end=' ', flush=True)
        sleep(0.3)
    print('END!')
    print('-='*20)


count1()
count2()
count3()