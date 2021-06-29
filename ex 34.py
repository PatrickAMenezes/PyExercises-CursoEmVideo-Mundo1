total_spent = more_than_thousand = quantity = cheaper_product = 0
while True:
    product_name = str(input('The name of the product: ')).strip()
    product_price = float(input('His price: R$ '))
    total_spent += product_price
    quantity += 1
    if product_price > 1000:
        more_than_thousand += 1
    if quantity == 1 or product_price < smaller:
        smaller = product_price
        cheaper_product = product_name
    cont = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
    while cont not in 'YN':
        cont = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'The amount is R${total_spent:.2f}. The quantity of products that costs over\n'
      f'than R$1000 is {more_than_thousand} and the cheaper product is {cheaper_product}.')
