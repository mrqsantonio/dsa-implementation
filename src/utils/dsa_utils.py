from sympy import isprime

# This function 

def get_prime_dividers(n):
    result = []
    for i in range(1, n):
        if ( n % i == 0 and isprime(i)):
            result.append(i)
    return result
