# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 23:33:29 2021

@author: kazuk
"""

mod = 10 ** 9 + 7
x, y = map(int, input().split())
mt = 2 * 10 ** 6
fact = [1] * (mt + 1)
for i in range(mt):
    fact[i + 1] = fact[i] * (i + 1) % mod
def inv(n):
    return pow(n, mod - 2, mod)

#vector1(2, 1)とvector2(1, 2)の組み合わせによってx, yに到達できるか
#vector1の数をa、vector2の数をbとする
ans = 0
for i in range(int(x // 2) + 1):
    a = i
    b = x - 2 * a
    if a + 2 * b == y:
        ans += fact[a + b] * inv(fact[a]) * inv(fact[b]) % mod

print(ans)