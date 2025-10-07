import pytest
from sympy import isprime

from utils.dsa_utils import *

# Tests if an exception is raised in case the parameter "list" is an empty list
def test_get_random_element_from_empty_list():
    with pytest.raises(Exception):
        get_random_element([])

# Tests if in 99 tries the random element fetch is always inside the constrain
def test_get_random_element():
    for i in range(1, 100):
        element = get_random_element(range(0, i))
        assert element >= 0 and element < i, f" element({element}) !in [0,{i})"

# Test if on a know non inversible number mod 8, 0 is returned
def test_mod_inverse_with_non_inversible():
    inverse = mod_inverse(2, 8)
    assert inverse == 0, f"Inverse found ({inverse}) for non inversible number."
