def increase (val = 0, tax = 0):
    res = val + (val*tax)/100
    return res


def decrease(val = 0, tax = 0):
    res = val - (val*tax)/100
    return res


def half(val = 0):
    res = val/2
    return res


def double(val = 0):
    res = val*2
    return res


def coin(val = 0, coin = 'R$'):
    return f'{coin}{val:.2f}'.replace('.', ',')
