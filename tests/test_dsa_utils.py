import pytest
from sympy import isprime

from utils.dsa_utils import get_prime_dividers, get_random_element

expected_results = [
    (0, []),
    (1, []),
    (2, []),
    (3, []),
    (4, [2]),
    (5, []),
    (6, [2, 3]),
    (7, []),
    (8, [2]),
    (9, [3]),
    (10, [2, 5]),
    (11, []),
    (12, [2, 3]),
    (13, []),
    (14, [2, 7]),
    (15, [3, 5]),
    (16, [2]),
    (17, []),
    (18, [2, 3]),
    (19, []),
    (20, [2, 5])
]

def test_prime_dividers():
    for pair in expected_results:
        prime_dividers = get_prime_dividers(pair[0])
        assert prime_dividers == pair[1], (
            f"Assertion failed for n={pair[0]} got {str(prime_dividers)}, while expecting {str(pair[1])}"
        )
        for i in prime_dividers:
            assert pair[0] % i == 0, f"{i} is not a prime divider of {pair[0]}"
            assert isprime(i), f"{i} is not prime"

def test_get_random_element_from_empty_list():
    with pytest.raises(Exception):
        get_random_element([])

def test_get_random_element():
    for i in range(1, 100):
        element = get_random_element(range(0, i))
        assert element >= 0 and element < i, f" element({element}) !in [0,{i})"
