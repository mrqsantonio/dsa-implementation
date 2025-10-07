from sympy import isprime
import random

def get_multiple_primes(q):
    result = []
    for i in range(2, 10):
        p = q * i + 1
        if isprime(p):
            result.append(p)
    return result

def get_random_element(list):
    if len(list) == 0:
        raise Exception("A empty list was found, while at least one value is required.")
    return list[random.randint(0, len(list) - 1)]

# n ^ -1 mod m
def mod_inverse(n, m):
    try:
        i = pow(n, -1, m)
        if (i * n) % m == 1:
            return i
    except ValueError:
        pass
    return 0
