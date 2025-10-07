import pytest

from dsa import *

def test_n_out_of_bounds():
    for n in (-1, 0, 1, 2):
        with pytest.raises(Exception) as info:
            get_DSAparameters(n)

# We are geneating a p inside the bit range and expecting q to be inside that range
# The requirement is q inside the range (is it right?)

def test_number_of_bits():
    max = 5
    for n in range(3, max):
        p, q, g = get_DSAparameters(n)
        assert ((q).bit_length() == n), (
            f"{q} has {(q).bit_length()} bit{'' if q == 1 else 's'} while expecting {n}."
        )

def test_get_skeys():
    p = 859
    q = 13
    g = 635
    for i in range(1, p * 100): # Since x is random we are trying to ensure that x is always within ]1, p - 1[
        x, y = get_skeys(p, q, g)
        assert x > 1 and x < q - 1

def test_dsa_sign():
    message = 13
    p = 23
    q = 11
    g = 196
    x = 4
    r, s = dsa_sign(message, p, q, g, x)
    assert True

