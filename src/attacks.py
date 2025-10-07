from utils.dsa_utils import mod_inverse

# Exercise 5
def get_private_key(y, g, p):
    if y <= 0 or g <= 0 or p <= 0:  # Ensures that all values are within bounds
        raise Exception("parameters must be postive non zero integers.")
    x = 2                           # 1 < x < q -1
    y_p = y % p                     
    g_x = pow(g, x) % p             # g^2 mod p
    while(y_p != (g_x)):            # y = g^x mod p
        g_x = g_x * g % p           # calculates g^(x + 1) based on g^x
        x += 1                      # increment x
    return x

# Exercise 6
# Having two messages, its respective signatures q and r
# If the same k is used, it is possible to obtain x
def get_private_key_from_k(m1, s1, m2, s2, r, q):
    return ((s2 * m1 - s1 * m2) * mod_inverse(r * (s1 - s2), q)) % q
