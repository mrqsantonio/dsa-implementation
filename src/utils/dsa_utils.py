from sympy import isprime
import random

# This function 

def get_prime_dividers(n):
    result = []
    for i in range(1, n):
        if n % i == 0 and isprime(i):
            result.append(i)
    return result

def get_random_element(list):
    if len(list) == 0:
        raise Exception("A empty list was found, while at least one value is required.")
    return list[random.randint(0, len(list) - 1)]
