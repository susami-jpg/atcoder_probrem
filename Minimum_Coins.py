# -*- coding: utf-8 -*-
"""
Created on Sun May  2 21:47:18 2021

@author: kazuk
"""

n = int(input())
a, b, c = map(int, input().split())
ans = 10 ** 5
for x in range(10 ** 4):
    for y in range(10 ** 4):
        if x + y > 10 ** 4 or n - (a * x + b * y) < 0:
            continue
        if (n - (a * x + b * y)) % c == 0:
            z = (n - (a * x + b * y)) // c
            ans = min(ans, x + y + z)
print(int(ans))
            
            
            
            

    

