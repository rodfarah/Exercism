def find(search_list: list, value: int) -> int:
    """In computer science, a binary search or half-interval search algorithm finds the position \
    of a specified input value (the search "key") within an array sorted by key value.
    In each step, the algorithm compares the search key value with the key value of the middle element\
    of the array.
    If the keys match, then a matching element has been found and its index, or position, is returned.
    Otherwise, if the search key is less than the middle element's key, then the algorithm repeats its \
    action on the sub-array to the left of the middle element or, if the search key is greater, on the \
    sub-array to the right.
    """
    min_idx = 0
    base_idx = (len(search_list)-1) // 2
    max_idx = len(search_list) - 1

    while base_idx >= min_idx and base_idx <= max_idx:
        if search_list[base_idx] == value:
            return base_idx
        else:
            if search_list[base_idx] > value:
                if search_list[base_idx - 1] < value:
                    break
                else:
                    base_idx -= 1
                    continue
            if search_list[base_idx] < value:
                if base_idx + 1 > len(search_list) - 1:
                    break
                elif search_list[base_idx + 1] > value:
                    break
                else:
                    base_idx += 1
                    continue
    raise ValueError('value not in array')


print(find([1, 3, 4, 6, 8, 9, 11], 2))
