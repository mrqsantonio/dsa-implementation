# Cybersecurity - DSA (Implementation & Attacks)

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
[![License](https://img.shields.io/badge/license-GPL--2.0-blue.svg)](LICENSE)


## Summary

This is an educational project in the context of the cybersecurity course @ISEL, it implements the core components of the **Digital Signature Algorithm (DSA)** and demonstrates two practical attacks:

1. **Brute-force discrete logarithm** (recovering the private key `x` by trying all candidate exponents).
2. **Reuse of ephemeral key `k`** (recovering the private key `x` when the same ephemeral `k` is used to sign two different messages).

The goal is pedagogical: to understand how DSA works (domain parameter generation, key generation, signing, verification) and to explore real vulnerabilities that can arise from poor randomness or parameter choices.

> **Warning:** This code is for educational only. Do **not** use it to sign real messages or to secure real systems. Key sizes used for examples/tests are small on purpose to make attacks feasible.

## Index
- [Structure](#structure)
- [Features](#features)
- [Dependencies](#dependencies)
    - [Install dependencies](#install-dependencies)
        - [On Windows](#on-windows)
        - [On Linux / macOS](#on-linux--macos)
- [Tests](#tests)
- [Metrics](#metrics)

---

# Structure

- pyproject.toml                    # General project information
- src
    - dsa.py                        # DSA implementation
    - attacks.py                    # Attacks implementation
    - utils
        - dsa_utils.py              # DSA support functions
- tests
    - test_dsa.py                   # Test DSA implementation
    - test_dsa_utils.py             # Test DSA support functions
    - test_attacks.py               # Test attacks implementation
    - metrics
        - test_dsa_metrics.py       # Generates metrics of DSA implementation
        - test_attacks_metrics.py   # Generates metrics of the DSA Attacks


---

# Features

The `dsa` module implements:

* `get_DSAparameters(n) -> (p, q, g)`
  Generate DSA domain parameters:

  * `q` — an `n`-bit prime,
  * `p` — a prime such that `q | (p - 1)`,
  * `g` — generator of a subgroup of order `q` modulo `p`.
    All returned values are Python `int`.

* `get_skeys(p, q, g) -> (x, y)`
  Generate a session private/public key pair:

  * `x` — private key integer (`0 < x < q`),
  * `y` — public key `y = pow(g, x, p)`.
    Both are `int`.

* `dsa_sign(message, p, q, g, x, k=None) -> (r, s)`
  Sign a `message` (bytes or `str`) returning `(r, s)` as integers.

  * The implementation uses a hash (e.g., SHA-1/SHA-256) of `message` where appropriate.
  * Optionally accepts `k` (ephemeral) to allow testing of `k` reuse attacks. If `k` is not provided, a secure random `k` is generated.

* `dsa_verify(message, signature, p, q, g, y) -> bool`
  Verify a signature `(r, s)` for `message` using public key `y`. Returns `True` if valid, `False` otherwise.

* `get_private_key(y, g, p) -> x or None`
  Brute-force discrete logarithm: iterate `x` from `1` to `p-1` (or `q-1` when appropriate) to find `x` such that `pow(g, x, p) == y`. Returns the private key `x` on success or `None` if not found. (Intended for tiny/moderate parameters only.)

* `recover_x_from_reused_k(r, s1, s2, m1, m2, q) -> x`
  Recover private key `x` when two signatures share the same `r` (i.e., same ephemeral `k` was used) using the formula:

  ```
  x = (s2*m1 - s1*m2) * inv(r * (s1 - s2), q) mod q
  ```

  where `m1, m2` are the integer hashes of messages and `inv()` is modular inverse modulo `q`.

---

# Dependencies

* Python 3.10+
* `sympy` — prime generation and number-theory utilities
* `pytest` — tests

## Install dependencies

### On Windows
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

### On Linux / macOS
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# Tests

Run unit tests with pytest:

```bash
pytest --cov=src --cov-report=term-missing
```

Tests cover:

* Domain parameter properties (`q | (p-1)`, `q` and `p` prime),
* Key generation and matching `y = g^x mod p`,
* Sign/verify correctness,
* `get_private_key` on tiny examples,
* `k` reuse attack recovers the correct `x`.

# Metrics
