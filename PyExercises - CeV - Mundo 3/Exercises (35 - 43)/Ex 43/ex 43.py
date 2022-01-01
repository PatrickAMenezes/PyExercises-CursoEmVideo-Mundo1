from Functions import people, menu
from Functions.line import line
while True:
    m = menu.menu()
    if m == 0:
        print('\033[1;32mFinished!\033[m'.center(55))
        line()
        break
    else:
        if m == 1:
            p = people.people()
            print(line(), end='\n')
            if p >= 1:
                print('Registering...'.center(44))
            for i in range(p):
                arch = open('teste.txt', 'a')
                arch.write(line())
                arch.write('\nName: ')
                print(line(), end='\n')
                while True:
                    try:
                        arch.write(str(input('Name: ').strip().title()) + '\n')
                    except:
                        print('Invalid insert.')
                    else:
                        break
                arch.write('Age: ')
                while True:
                    try:
                        age = int(input('Age: '))
                        if age < 0:
                            print('Invalid age.')
                            continue
                    except:
                        print('Invalid age.')
                    else:
                        arch.write(str(age) + '\n')
                        break
                print(line(), end = '\n')
                arch.write(line() + '\n')
                if i == p:
                    arch.close()
        else:
            try:
                arch = open('teste.txt', 'r')
                print(line())
                print('Listing...'.center(44))
                print(arch.read())
            except FileNotFoundError:
                print(line())
                print('Non-existent file'.center(45))
                print(line())
