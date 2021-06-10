# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:25:30 2021

@author: kazuk
"""

n = int(input())
def check(s):
    if '7' in s:
        return False
    else:
        return True

ans = 0
for i in range(1, 1+n):
    s = set(str(i))
    if check(s):
        os = set(oct(i)[2:])
        if check(os):
            ans += 1

print(ans)
    
    
    