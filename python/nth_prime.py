'''Given a number n, determine what the nth prime is. By listing the \
first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that \ 
the 6th prime is 13.
'''


def prime(number: int) -> int:
    if number == 0:
        raise ValueError('there is no zeroth prime')
    elif number < 0:
        raise ValueError('number must be a positive integer')

    n = 2
    primes = [2]
    while len(primes) < number:
        n += 1
        check_list = []
        if all(n % p > 0 for p in primes):
            primes.append(n)
        

    return primes[number - 1]


print(prime(10001))
