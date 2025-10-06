
def get_private_key(y, g, p):
    if y <= 0 or g <= 0 or p <= 0:
        raise Exception("parameters must be postive non zero integers.")
    x = 2 # 1 < x < q -1
    y_p = y % p
    g_x = pow(g, x) % p
    while(y_p != (g_x)):
        g_x = g_x * g % p
        x += 1
    return x

# Having two messages, its respective signatures q and r
# If the same k is used, it is possible to obtain x
def get_private_key_from_k(m1, s1, m2, s2, r, q):
    divider = r * (s1 - s2)     # In DSA r can never be zero, so according to spec if s1 != s2 all is good.
    if divider == 0:
        raise ZeroDivisionError("s1 must be different from s2.")
    return ((s2 * m1 - s1 * m2) / divider) % q
