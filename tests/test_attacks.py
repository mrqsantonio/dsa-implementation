import pytest

from attacks import get_private_key, get_private_key_from_k

# Test if for a known example the brute force attack works
def test_get_private_key():
    p = 23                          # small prime
    g = 5                           # generator
    original_x = 7                  # private key
    y = pow(g, original_x) % p      # public key (17)

    x = get_private_key(y, g, p)    # brute force result
    assert x == original_x, f"Expecting x to be {original_x} but got {x}"

# Test if the function handles values of out of bounds by raising an exception
def test_get_private_key_bounds():
    out_of_bounds_pairs = [
        (17, 5, 0),
        (17, 0, 23),
        (0, 5, 23),
        (17, 0, 0),
        (0, 0, 23),
        (0, 5, 0),
        (0, 0, 0)
    ]
    for pair in out_of_bounds_pairs:
        with pytest.raises(Exception):
            x = get_private_key(pair[0], pair[1], pair[2])
            assert False, f" For {str(pair)} x = {x}."

# Tests if for a know example the key repetition attack works
def test_get_private_key_from_k():
    x = 7
    m1 = 10
    s1 = 14
    m2 = 15
    s2 = 8
    r  = 21
    q  = 23
    x_candidate = get_private_key_from_k(m1, s1, m2, s2, r, q)  # ((s2 * m1 - s1 * m2) / (r * (s1 - s2))) % q
    assert x_candidate == x, f"x = {x_candidate} with expecting {x}"