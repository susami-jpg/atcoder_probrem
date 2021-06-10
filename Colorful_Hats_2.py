# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:02:38 2021

@author: kazuk
"""

mod = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
rest = [0] * (n + 1)
rest[0] = 3
ans = 1
for i in range(n):
    now = a[i]
    ans *= rest[now]
    rest[now] -= 1
    rest[now + 1] += 1

print(max(ans, 0) % mod)

    

    
        

