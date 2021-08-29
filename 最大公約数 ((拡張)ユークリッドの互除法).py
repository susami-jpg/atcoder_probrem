# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:25:23 2021

@author: kazuk
"""

# Euclidean Algorithm
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

# Euclidean Algorithm (non-recursive)
def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m

# Extended Euclidean Algorithm
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

def extGCD(a,b):
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y

# lcm (least common multiple)
def lcm(m, n):
    return m//gcd(m, n)*n

#5 3つ以上の数の最大公約数を計算する
def gcd_t(list_g1):
    for i in reversed(range(1, min(list_g1)+1)):
        for j in list_g1:
            if j%i!=0:
                break
        else:
            return i

#10 最大の数の倍数から最小公倍数を計算
def lcm(list_l):
    greatest = max(list_l)
    i = 1
    while True:
        for j in list_l:
            if (greatest * i) % j != 0:
                i += 1
                break
        else:
            return greatest * i