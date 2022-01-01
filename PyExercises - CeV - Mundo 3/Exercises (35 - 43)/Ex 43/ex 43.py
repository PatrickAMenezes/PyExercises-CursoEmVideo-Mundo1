from Functions import people, menu
while True:
    m = menu.menu()
    if m == 0:
        print('\033[1;32mFinished!\033[m')
        break
    else:
        if m == 1:
            p = people.people()
            print('-'*30, end='\n')
            print('Registering...')
            for i in range(p):
                arch = open('teste.txt', 'a')
                arch.write('-'*30)
                arch.write('\nName: ')
                print('-'*30, end='\n')
                arch.write(str(input('Name: ').strip().title()) + '\n')
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
                print('-'*30, end = '\n')
                arch.write('-'*30 + '\n')
                if i == p:
                    arch.close()
        else:
            try:
                arch = open('teste.txt', 'r')
                print('-'*30)
                print('Listing...')
                print(arch.read())
            except FileNotFoundError:
                print('-'*30)
                print('Non-existent file.')
                print('-'*30)
