# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:03:22 2021

@author: kazuk
"""

n = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#float型の数値が整数（小数点以下が0）か判定: float.is_integer()
def check(l):
    a = n/l - l/2 + 1/2
    return a.is_integer()

ans = 0
for l in make_divisors(2 * n):
    if check(l):
        ans += 1
print(ans)
    
    