# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:10:40 2021

@author: kazuk
"""

n = 10 ** 5
#エラストテネスの篩による素数判定
prime = [1] * (n + 1)
prime[0] = prime[1] = 0
for i in range(2, n + 1):
    if prime[i] == 1:
        for j in range(i * i, n + 1, i):
            prime[j] = 0
            
#2017likeかどうかの判定
like2017 = [0] * (n + 1)
for i in range(n + 1):
    if i % 2 == 0 or prime[i] == 0:
        continue
    query = int((i + 1) // 2)
    if prime[query]:
        like2017[i] = 1

#累積和をとる
for i in range(n):
    like2017[i + 1] += like2017[i]

q = int(input())
ans = []
for _ in range(q):
    l, r = map(int, input().split())
    ans.append(like2017[r] - like2017[l - 1])

for i in ans:
    print(i)
    