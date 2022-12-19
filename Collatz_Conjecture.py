def steps(number):
    if isinstance(number, int) and number > 0:
        try_n = 1
        while number != 1:
            if number % 2 == 0:
                number = number / 2
                try_n += 1
            else:
                number = number * 3 + 1
                try_n += 1
    else:
        raise ValueError('Only positive integers are allowed')
    return try_n - 1


print(steps(0))
