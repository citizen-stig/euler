#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

num = 600851475143


def is_prime(number):
    for i in range(2, int(math.ceil(math.sqrt(number)))):
        if number % i == 0:
            return False
    return True


max_prime_factor = 0

for i in range(3, int(math.ceil(num / 2))):

    if num % i == 0:
        print('Checking {0}'.format(i))
        if is_prime(i):
            if i > max_prime_factor:
                print('++++++++++++++')
                max_prime_factor = i
                print(max_prime_factor)
                print('++++++++++++++')

print(max_prime_factor)