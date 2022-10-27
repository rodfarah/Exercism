def sum_of_multiples(limit, multiples):

    for nums in multiples:
        if nums == 0:
            multiples.remove(0)

    number_list = []
    for num in range(limit):
        for mult in multiples:
            if num == 0:
                number_list = [0]
                break
            elif num % mult == 0:
                number_list.append(num)

    return sum(set(number_list))
