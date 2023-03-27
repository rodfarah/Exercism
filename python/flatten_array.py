def flatten(iterable):

    list_of_numbers = []

    for item in iterable:
        if type(item) is int:
            list_of_numbers.append(item)
        elif type(item) is list:
            list_of_numbers += flatten(item)

    return list_of_numbers


print(flatten([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]))
