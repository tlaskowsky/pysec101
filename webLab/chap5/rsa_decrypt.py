#!/usr/bin/python
#-*- coding: utf-8 -*-

def ex_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = ex_gcd(b%a, a)
        return gcd, y - int(b/a) * x, x

def gen_private_key(e, phi_n):
    gcd, d, y = ex_gcd(e, phi_n)
    if d < 0:
        d += phi_n
    return d

def decrypt(cipher):
    e = 65537
    p, q = 513131, 248021
    n = p*q
    phi_n = (p-1)*(q-1)
    plain = []

    d = gen_private_key(e, phi_n)

    for c in cipher:
        m = pow(c, d, n)
        plain.append(chr(m))
    return ''.join(plain)

if __name__=='__main__':
    cipher = [86236114022, 118116081811, 54504123396, 54504123396, 48679148382, 49643963012]
    result = decrypt(cipher)
    print('plain text:')
    print(result),
