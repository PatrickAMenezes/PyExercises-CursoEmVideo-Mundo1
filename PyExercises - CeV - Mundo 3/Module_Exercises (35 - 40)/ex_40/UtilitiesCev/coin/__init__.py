def increase (val=0, tax=0, form=False):
    res = val + (val*tax)/100
    return res if form is False else coin(res)


def decrease(val=0, tax=0, form=False):
    res = val - (val*tax)/100
    return res if form is False else coin(res)


def half(val=0, form=False):
    res = val/2
    return res if form is False else coin(res)

def double(val=0, form=False):
    res = val*2
    return res if form is False else coin(res)


def coin(val=0, coin='R$'):
    res = f'{coin}{val:.2f}'.replace('.', ',')
    return res


def resume(val=0, inc=0, dec=0):
    print('-'*45)
    print('VALUE SUMMARY'.center(45))
    print('-'*45)
    print(f'Analyzed price: {" "*10}{coin(val)}.')
    print(f'Half-price: {" "*14}{half(val, True)}.')
    print(f'Double the price: {" "*8}{double(val, True)}.')
    print(f'{inc}% increase: {" "*12}{increase(val, inc, True)}.')
    print(f'{dec}% decrease: {" "*13}{decrease(val, dec, True)}.')
    print('-'*45)
    print('END'.center(45))
    print('-'*45)
