import random

from sympy import randprime
from utils.dsa_utils import *

# Exercise 1
def get_DSAparameters(n): 
    if(n < 3): 
        raise Exception("n must be at least 3.")
    q = randprime(pow(2, n - 1), pow(2, n))         # generate a prime q inside with n bits
    p_candidates = get_multiple_primes(q)           # get prime numbers where p = q * i + 1
    p = get_random_element(p_candidates)            # select a random p from the candidates

    g = 1
    while(g == 1):                                  # Calculating h, so that g != 1 mod p
        h = get_random_element(range(2, p - 1))     # range é [2,p-1[
        g = int(pow(h, (p - 1) / q) % p)            # g is congruent mod p
    return p, q, g

# Exercise 2
def get_skeys(p, q, g):
    x = get_random_element(range(2, q - 1))         # 1 < x < q - 1
    y = pow(g, x) % p                               # y = (g^x) mod p
    return x, y

# Exercise 3
def dsa_sign(message, p, q, g, x):
    r = 0
    s = 0
    while(r == 0 or s == 0):                        # executes at least once
        k = get_random_element(range(2, q - 1))     # 1 < k < q - 1
        r = pow(g, k, p) % q                        # r = (g^k mod p) mod q
        k_inverse = mod_inverse(k, q)               # inverse of k mod q
        s = (k_inverse * (message + r * x)) % q     # if k doesnt have inverse s will be 0
    return r, s

# Exercise 4
def dsa_verify(message, signature, p, q, g, y):
    r = signature[0]
    s = signature[1]
    if r < 1 or r >= q or s < 1 or s >= q:          # 0 < r < q and 0 < s < q
        raise Exception("Invalid signature.")
    w = mod_inverse(s, q)                           # w = s^-1 (mod q)
    u1 = (message * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1 ) * pow(y, u2 )) % p             # v = ((g^u1) * (u^u2)) mod p
    v %= q                                          # v = v mod q
    return v == r
