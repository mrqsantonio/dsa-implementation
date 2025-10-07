import random

from sympy import randprime
from utils.dsa_utils import *

# Exercise 1
def get_DSAparameters(n): 
    if(n < 3): 
        raise Exception("N must be at least 3")
    q = randprime(pow(2, n - 1), pow(2, n))     # is randprime inclusive?
    p_candidates = get_multiple_primes(q)
    p = get_random_element(p_candidates)

    # Calculating h, so that g != 1 mod p
    g = 1
    while(g == 1):
        h = get_random_element(range(2, p - 1)) # range é [2,p-1[
        g = pow(h, (p - 1) / q)                 # g is congruent mod p
    return p, q, g

# Exercise 2
def get_skeys(p, q, g):
    x = get_random_element(range(2, q - 1))
    y = pow(g, x) % p
    return x, y

# Exercise 3
def dsa_sign(message, p, q, g, x):
    r = 0
    s = 0
    while(r == 0 or s == 0):
        k = get_random_element(range(2, q - 1))
        r = pow(g, k, p) % q
        k_inverse = mod_inverse(k, q)   # inverse of k mod q
        s = (k_inverse * (message + r * x)) % q
    return r, s

# Exercise 4
def dsa_verify(message, signature, p, q, g, y):
    r = signature[0]
    s = signature[1]
    if r < 1 or r >= q or s < 1 or s >= q:
        raise Exception("Invalid signature.")
    w = mod_inverse(s, q)
    u1 = (message * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1 ) * pow(y, u2 )) % p
    v %= q
    print(str(v))
    return v == r
