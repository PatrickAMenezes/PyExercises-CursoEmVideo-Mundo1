from random import choice
a1 = str(input('The name of the first student: '))
a2 = str(input('The second: '))
a3 = str(input('The third: '))
a4 = str(input('The fourth: '))
students = [a1, a2, a3, a4]
chosen = choice(students)
print('O aluno escolhido pra apagar o quadro é {}'.format(chosen))
