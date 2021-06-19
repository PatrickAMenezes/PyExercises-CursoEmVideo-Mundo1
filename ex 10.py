from time import sleep
from emoji import emojize
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('HAPPY NEW YEAR!!!!!', end='')
print(emojize(':fireworks::tada:', use_aliases=True))
