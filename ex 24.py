nome = str(input('Digite um nome completo: ')).title()
print('O primeiro nome é {} e o último é {} '
    .format(nome.split()[0], nome.split()[-1]))
