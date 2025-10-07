from sympy import isprime
import random

def get_multiple_primes(q):
    result = []
    i = 2
    while i < 10 or len(result) < 0:    # Ensures at least one value
        p = q * i + 1
        if isprime(p):
            result.append(p)
        i += 1
    return result

def get_random_element(list):
    if len(list) == 0:
        raise Exception("A empty list was found, while at least one value is required.")
    return list[random.randint(0, len(list) - 1)]

# n ^ -1 mod m
def mod_inverse(n, m):
    try:
        return pow(n, -1, m)                # Calculates inverse of n mod m
    except ValueError:
        pass                                # If n does not has an inverse mod m, returns 0
    return 0                                # The Caller has the responsability to expect this behaviour
