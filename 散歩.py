# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 01:33:07 2021

@author: kazuk
"""

mod = 10 ** 9 + 7
n, q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
c.insert(0, 1)
c.append(1)
cumsum = [0] * n
for i in range(n - 1):
    cumsum[i + 1] = cumsum[i] + pow(a[i], a[i + 1], mod)

ans = 0
for i in range(len(c) - 1):
    now = c[i] - 1
    nexttown = c[i + 1] - 1
    ans += abs(cumsum[nexttown] - cumsum[now]) % mod
print(ans % mod)
