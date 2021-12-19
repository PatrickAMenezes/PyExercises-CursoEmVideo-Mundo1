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
