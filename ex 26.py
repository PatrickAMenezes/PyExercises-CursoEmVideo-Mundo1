from time import sleep
def counter(beggining, final, step):
    print('-='*20)
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print(f'Counting from {beggining} to {final} of {step} in {step}:')
    if final > beggining:
        final += 1
    else:
        final -= 1
        if step > 0:
            step *= -1
    for c in range (beggining, final, step):
        print(c, end=' ', flush=True)
        sleep(0.3)
    print('END!')
    print('-='*20)


counter(1, 10, 1)
counter(10, 0, 2)
print('Now it\'s your turn.')
b = int(input('Beggining: '))
f = int(input('Final: '))
s = int(input('Step: '))
counter(b, f, s)
