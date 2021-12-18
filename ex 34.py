def manual(command):
    from time import sleep
    sleep(1)
    print('\033[0;40m')
    help(command)
    sleep(2)


def title(msg, color=0):
    print(color, f'----- {msg} -----')


while True:
    title('PYTHON HELP SYSTEM', '\033[1;30;44m')
    cmd = str(input('\033[mFunction or library to search(stop to finish the program): ')).strip().lower()
    if cmd == 'stop':
        title('FINISHED', '\033[1;30;42m')
        break
    else:
        title(f'Acessing the manual of the {cmd} command...', '\033[1;30;41m')
        manual(cmd)
