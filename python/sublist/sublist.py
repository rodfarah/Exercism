
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """Return either one list is equal, superlist, sublist or unequal to other list."""
    if list_one == list_two:
        return 3
    elif len(list_one) < len(list_two):
        idx = 0
        while idx <= len(list_two) - len(list_one):
            if list_two[idx:len(list_one)+idx] == list_one:
                return 1
            idx += 1
    elif len(list_one) > len(list_two):
        idx = 0
        while idx <= len(list_one) - len(list_two):
            if list_one[idx:len(list_two)+idx] == list_two:
                return 2
            idx += 1
    return 4
