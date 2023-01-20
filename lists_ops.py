from functools import reduce


def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    result = []
    idx = 0
    while idx <= len(lists) - 1:
        for item in lists[idx]:
            result.append(item)
        idx += 1
    return result


def filter(func, any_list):

    return [item for item in any_list if func(item)]


def length(list):
    return len(list)


def map(func, any_list):
    result_list = []
    for item in any_list:
        result_list.append(func(item))

    return result_list


def foldl(func, any_list, initial):
    result = reduce(func, any_list, initial)
    return result


def foldr(func, any_list, initial):
    list_2 = any_list[::-1]
    for item in list_2:
        initial = func(item, initial)
    return initial


def reverse(any_list):
    return any_list[::-1]
