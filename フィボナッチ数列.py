# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:47:10 2021

@author: kazuk
"""

n = int(input())
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(n))

#計算量が増大していかないようにメモをとる
N = 45
dp = [0] * N
dp[0] = dp[1] = 1
for i in range(N-2):
    dp[i+2] = dp[i] + dp[i+1]
n = int(input())
print (dp[n])