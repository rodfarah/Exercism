def sum_of_num(*args):

    el = []

    for arg in args:
        el.append(arg)
    
    return sum(el)

print(sum_of_num(4))