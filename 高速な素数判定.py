# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:06:52 2021

@author: kazuk
"""

from math import sqrt
n = int(input())

#高速な素数判定
def isprime(x):
  if x == 2:
    return True

  if x < 2 or x % 2 == 0:
    return False

  i = 3
  while i <= sqrt(x):
    if x % i == 0:
      return False
    i += 2

  return True

#エラストテネスの篩
N = 10**6
dp = [1] * (N+1)
dp[0] =  dp[1] =  0

for i in range(2,N+1):
    if dp[i]:
        for j in range(i*i, N+1, i):
            dp[j] = 0

ans = 0
for _ in range(n):
    if dp[int(input())]:
        ans += 1

print(ans)
