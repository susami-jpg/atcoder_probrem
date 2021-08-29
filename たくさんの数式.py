# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:26:40 2021

@author: kazuk
"""

s = list(input())

def stoi(s):
    return int("".join(s))

n = len(s) - 1
ans = 0
for i in range(1 << n):
    l = 0
    cnd = 0
    for j in range(n):
        if (i >> j) & 1:
            cnd += stoi(s[l:j+1])
            l = j + 1
    cnd += stoi(s[l:])
    ans += cnd
print(ans)

    
            
        
        
