print('='*40)
print(f'{"PRICE LISTING":^40}')
print('='*40)
products = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas',
            22.30, 'Livro', 34.90)
for c in range (0, 18, 2):
    print(f'{products[c]:.<30}R${products[c+1]:>6.2f}')
print('='*40)
