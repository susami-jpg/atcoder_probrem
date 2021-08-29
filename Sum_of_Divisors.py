# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:47:25 2021

@author: kazuk
"""

n = int(input())

def num_divisors_table(n):
    table = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1
    
    return table

ans = 0
table = num_divisors_table(n)
for i, num in enumerate(table):
    ans += i * num

print(ans)
