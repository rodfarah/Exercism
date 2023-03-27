'''Given a number n, determine what the nth prime is. By listing the \
    first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that \ 
    the 6th prime is 13.'''


def prime(number: int) -> int:
    if number == 0:
        raise ValueError('there is no zeroth prime')
    elif number < 0:
        raise ValueError('number must be a positive integer')

    prime_list = [2]
    next_one = 3
    while number >= len(prime_list):
        condition = True
        for p in prime_list:
            if next_one % p == 0:
                condition = False
                break
        if condition is False:
            next_one += 2
            continue
        for n in range(2, next_one):
            if next_one % n == 0:
                break
        prime_list.append(next_one)
        next_one += 2

    return prime_list[number - 1]
print(prime(10001))