import pytest

from dsa import *

# Test if a execption is raised if n < 3
def test_n_out_of_bounds():
    for n in (-1, 0, 1, 2):
        with pytest.raises(Exception) as info:
            get_DSAparameters(n)

# Test if for 2 < n < 5 q as the corresponding number of bits
def test_number_of_bits():
    max = 5
    for n in range(3, max):
        p, q, g = get_DSAparameters(n)
        assert ((q).bit_length() == n), (
            f"{q} has {(q).bit_length()} bit{'' if q == 1 else 's'} while expecting {n}."
        )

# Test for a known example if 1 < x < p - 1
def test_get_skeys():
    p = 859
    q = 13
    g = 635
    for i in range(1, p * 100): # Since x is random we are trying to ensure that x is always within ]1, p - 1[
        x, y = get_skeys(p, q, g)
        assert x > 1 and x < q - 1

# Test if for a known example sign and verify are sucessful
def test_dsa_sign_and_verify():
    message = 10
    p = 23
    q = 11
    g = 18
    x = 3
    y = 13
    r, s = dsa_sign(message, p, q, g, x)
    signature = (r, s)
    t = dsa_verify(message, signature, p, q, g, y)
    assert t, f"Failed to verify signature with r={r} and s={s}"

# Test if an exception is raised when 0 < r < q or 0 < s < q is not true
def test_dsa_verify_invalid_parameters():
    message = 10
    p = 23
    q = 11
    g = 18
    y = 13
    # r = 0, r = q, s = 0, s = q
    invalid_parameters = [
        (0, 10),
        (q, 10),
        (5, 0),
        (5, q),
        (0, 0),
        (0, q),
        (q, q)
    ]
    with pytest.raises(Exception) as info:
        for signature in invalid_parameters:
            dsa_verify(message, signature, p, q, g, y)
