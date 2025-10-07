# Cybersecurity - DSA (Implementation & Attacks)
![Static Badge](https://img.shields.io/badge/Cyber_Security-ISEL-darkred)
![Python](https://img.shields.io/badge/python-3.10-darkred.svg)
[![License](https://img.shields.io/badge/license-GPL--2.0-darkred.svg)](LICENSE)

This is an educational project in the context of the cybersecurity course @ISEL, it implements the core components of the **Digital Signature Algorithm (DSA)** and demonstrates some possible attacks

> **Warning:** This code is for educational only. Do **not** use it to secure real systems. Key sizes used for examples/tests are small on purpose and multiple constrains are ignored to make attacks feasible.

## Index
- [Project Structure](#project-structure)
- [DSA](#dsa)
  - [Algorithm](#algorithm)
    - [Domain Parameters](#domain-parameters)
    - [Session Keys](#session-keys)
    - [Signature Parameters](#signature-parameters)
  - [Constrains](#constrains)
- [Dependencies](#dependencies)
    - [Install dependencies](#install-dependencies)
        - [On Windows](#on-windows)
        - [On Linux / macOS](#on-linux--macos)
- [Running Tests](#running-tests)
- [TUI Mode](#tui-mode)
  - [Running the program](#running-the-program)
  - [Content](#content)
- [Attacks](#attacks)
  - [Brute Force](#brute-force)
    - [Algorithm](#algorithm-1)
    - [Example](#example)
    - [Result](#result)
    - [Metrics](#metrics)
  - [Key repetition](#key-repetition)
    - [Algorithm](#algorithm-2)
    - [Example](#example-1)
    - [Result](#result-1)
    - [Metrics](#metrics-1)

---

# Project Structure

- pyproject.toml                    - General project information
- src
    - dsa.py                        - DSA implementation
    - attacks.py                    - Attacks implementation
    - utils
        - dsa_utils.py              - DSA support functions
- tests
    - test_dsa.py                   - Test DSA implementation
    - test_dsa_utils.py             - Test DSA support functions
    - test_attacks.py               - Test attacks implementation
    - metrics
        - test_attack_metrics.py   - Generates metrics for the brute force attack


---

# DSA

## Algorithm

> **Warning:** This algorithm is not quantum-safe.

The DSA states the existence of [Domain Parameters](#domain-parameters), [Session Keys](#session-keys) and [Signature Parameters](#signature-parameters).

Since a signature is generated in the scope of a session, which as its domain parameters, said signature will be made from the following steps:

- Generate domain
  - Choose a random prime `q` of `n` bits.
  - Calculate a random prime `p`.
  - Generate `h` and `g` until `g != 1`.
- Generate session keys
  - Choose a random `x` from range.
  - Calculate `y`
- Sign a message
  - Generate ephemoral key `k` from range.
  - Calculate `r`
  - Use message to generate `s`
  - Repeat sign steps until `r` and `s` are different than 0.

### Domain parameters
The domain parameters are `p`, `q` and `g`, each parameter is obtain using the following method:

- `q` is a random prime number of `n` bits.
- `p = q * i + 1` where `i` is a random `integer` that ensures that p is a prime number.
- `g`

### Session keys
The session keys are generated based on the [Domain Parameters](#domain-parameters) and consists of a private key: `x` and a public key: `y`. This keys are generated as follows:

- `x` is a random `integer` that ensures `1 < x < q - 1`
- `y = (g ^ x) mod p`

In this pair, `x` **MUST** be keept secret at all times and `y` can be publicly known, all though to ensure that the signature is valid `y` must be transmitted trought a trusted channel (otherwise it allows a Men In The Middle Attack).

### Signature Parameters
To provide a signature of the message `m`, is necessary to generate a one time key `k`.

- `k` is a random `integer` that ensures `1 < k < q - 1`

> **Note:** `k`is not a signature parameter. It is an internal value, that **MUST** remain private and be used only once before being generated again.

The resulting values that compose a signature are `r` and `s`, which are computed using the following methods:

- `r mod q = ((g ^ k) mod p) mod q`.
- `s = ((m + x * r) / k) mod q`.
- where `k` must ensure that `r != 0 ` and `s != 0`

The implementation garantees that `r != 0` and `s != 0` by generating a new `k` and recalculating `r` and `s` each time the constraint is not met.

> **Note:** This algorithm is prone to brute force attacks, but since it uses multiple [Constrains](#constrains) and typically only accepts huge numbers, it makes the required computacional power required to consistently acquire the private key to expensive for real use case.

## Constrains
The current implementation takes in mind the following constrains:

1. `p` and `q` are prime numbers.
2. `p = q * i + 1` where `i` is a random `integer` that ensures (1).
3. `g != 1`
4. `1 < h <  p - 1` where h is a random `integer` that ensures (3).

5. `1 < x < q - 1`

6. `r > 0`
7. `s > 0`
8. `1 < k <  q - 1` where k is a random `integer` that ensures (6) and (7).


---

# Dependencies

* Python 3.10
* `sympy` - prime generation and number-theory utilities
* `pytest` - tests
* `pytest-cov` - tests coverage

## Install dependencies

### On Windows
```
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

### On Linux / macOS
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# Running Tests

Run unit tests with pytest:
`pytest --cov=src --cov-report=term-missing`

# TUI Mode
This project includes a text user interface mode to try the implementation from your console of choice.

## Running the program
`python src/main.py`

## Content
The TUI allows to:
- Create a domain (overrides old domain)
- Create a session (overrides old session)
- Sign a message (require a domain and session)
- Verify a message (require a domain and session)
- Restore session

# Attacks

This algorithm is prone to [Brute Force](#brute-force) and [Key repetition](#key-repetition) attacks.
This section consists in the explanation, analisys and execution of this to types of attacks.

## Brute force

This attack is based on trial and error and since the examples used on this attack consists on small numbers, the pool of results as an amount that makes fesable (due to time constrains) to calculate all possible values to find the coorect on.

### Algorithm
with the expression 
  -y = g^x (modp) and a 1 < x < q -1, 
the algorithm is basically testing all possible values of x starting from the lowest to find the private key
### Example
to make the metrics more accurate we're using 5 examples:
### Result
this were the result's of the examples above:
### Metrics
And by averaging the result's we get:
## Key repetition

### Algorithm
for the algorithm we know that ephemeral key(k) is repeated in both messages so if you look at the way the message is signed: 
  -s = k^−1 (m + x r )modq,
we can get to formula for the private Key:
  -x = (s2m1 − s1m2)(r (s1 − s2))−1 modq.
### Example
to make the metrics more accurate we're using 5 examples:
### Result
this were the result's of the examples above:
### Metrics
And by averaging the result's we get:
