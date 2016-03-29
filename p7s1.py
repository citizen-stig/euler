# -*- encoding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = [2, 3, 5, 7, 11, 13]


def find_next_prime():
    next_candidate = primes[-1]
    while True:
        next_candidate += 1
        for i in primes:
            if next_candidate % i == 0:
                break
        else:
            break
    return next_candidate


def find_n_prime(n):
    while len(primes) < n:
        next_prime = find_next_prime()
        primes.append(next_prime)
    return primes[-1]

print(find_n_prime(10001))
