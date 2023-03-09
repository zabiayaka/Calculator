def evaluate(x,y,z):
    result_1 = None
    if z == 1:
        result_1 = x+y
    elif z == 2:
        result_1 = x-y
    elif z == 3:
        result_1 = x*y
    elif z == 4:
        result_1 = x/y
    return result_1 