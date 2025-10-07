import pytest
from sympy import isprime

from utils.dsa_utils import *

def test_get_random_element_from_empty_list():
    with pytest.raises(Exception):
        get_random_element([])

def test_get_random_element():
    for i in range(1, 100):
        element = get_random_element(range(0, i))
        assert element >= 0 and element < i, f" element({element}) !in [0,{i})"

def test_mod_inverse_with_non_inversible():
    inverse = mod_inverse(2, 8)
    assert inverse == 0, f"Inverse found ({inverse}) for non inversible number."
