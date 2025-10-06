import random

from sympy import randprime
from utils.dsa_utils import get_multiple_primes, get_random_element

# Exercise 1
# This function i
def get_DSAparameters(n): 
    if(n < 3): 
        raise Exception("N must be at least 3")
    q = randprime(pow(2, n - 1), pow(2, n))
    p_candidates = get_multiple_primes(q)
    p = get_random_element(p_candidates)

    # Calculating h, so that g != 1 mod p
    g = 1
    while(g == 1):
        h = get_random_element(range(1, p - 1))
        g = pow(h, (p - 1) / q) % p # FIXME: this must be congruent with g not equal
    return p, q, g

def get_skeys(p, q, g):
    x = random.randint(1, q - 1)
    y = pow(g, x) % p
    return x, y

def dsa_sign(message, p, q, g, x):
    k = random.randint(1, q - 1)
    subR = pow(g, k) % p
    r = subR % q
    while(r == 0):
        k = random.randint(1, q - 1)
        subR = pow(g, k) % p
        r = subR % q
    inverseOfK = inverseOfNModP(k, q)
    xr = r * x
    s = (inverseOfK * (message + xr)) % q
    return r, s

def inverseOfNModP(n,p):
    phiOfN = p - 1
    return pow(n,phiOfN - 1) % p

def dsa_verify(message,signature,p,q,g,y):
    if(signature[0] > 0 and signature[0] < q and 
       signature[1] > 0 and signature[1] < q):
        print("r e s are OK")
    else:
        return False
    w = inverseOfNModP(signature[1]) % Q
    u1 = (message * w) % q
    u2 = (signature[0] * w) % q
    v= ((pow(g, u1 ) * pow(y, u2 )) % p) % q
    return v == signature[0]
