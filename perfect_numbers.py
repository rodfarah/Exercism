def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum_of_factors = sum([num for num in list(
        range(1, number)) if number % num == 0])

    if number <= 0:
        raise ValueError(
            'Classification is only possible for positive integers.')
    elif sum_of_factors == number:
        return 'perfect'
    elif sum_of_factors > number:
        return 'abundant'
    else:
        return 'deficient'
