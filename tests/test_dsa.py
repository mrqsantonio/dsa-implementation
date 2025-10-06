import pytest

from dsa import get_DSAparameters

def test_n_out_of_bounds():
    for n in (-1, 0, 1, 2):
        with pytest.raises(Exception) as info:
            get_DSAparameters(n)

# We are geneating a p inside the bit range and expecting q to be inside that range
# The requirement is q inside the range (is it right?)

def test_number_of_bits():
    max = 10
    for n in range(3, max):
        p, q, g = get_DSAparameters(n)
        assert ((q).bit_length() == n), (
            f"{q} has {(q).bit_length()} bit{'' if q == 1 else 's'} while expecting {n}."
        )
