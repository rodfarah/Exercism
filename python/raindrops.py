def convert(number):
    pling = (number % 3 == 0)
    plang = (number % 5 == 0)
    plong = (number % 7 == 0)

    result_list = []
    if pling:
        result_list.append('Pling')
    if plang:
        result_list.append('Plang')
    if plong:
        result_list.append('Plong')
    if len(result_list) == 0:
        return str(number)

    return ''.join(result_list)
