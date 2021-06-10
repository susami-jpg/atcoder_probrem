# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:20:45 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
inf = 10 ** 5
def poloc(n):
    return n*(n+1)*(n+2)//6

N = 10 ** 6
dp = [inf] * (N + 1)
dp_odd = [inf] *(N + 1)
dp[0] = dp_odd[0] = 0

for n in range(1, 10**3):
    p = poloc(n)
    if p > N:
        break
    for i in range(N-p+1):
        new = dp[i] + 1
        if dp[i + p] > new:
            dp[i + p] = new
    if p & 1:
        for i in range(N-p+1):
            new = dp_odd[i] + 1
            if dp_odd[i + p] > new:
                dp_odd[i + p] = new

while 1:
    n = int(input())
    if n == 0:
        break
    print(dp[n], dp_odd[n])

    
        
        
        
        
        
        
    