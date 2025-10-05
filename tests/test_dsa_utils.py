import pytest

from utils.dsa_utils import get_prime_dividers

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
