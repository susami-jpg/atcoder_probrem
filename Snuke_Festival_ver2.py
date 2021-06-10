# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:45:26 2021

@author: kazuk
"""

from bisect import bisect_left, bisect_right
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
a.sort()
c.sort()
for i in b:
    a_cnd = bisect_left(a, i) # 挿入点はどの同じ値よりも左
    c_cnd = bisect_right(c, i) # 挿入点はどの同じ値よりも右
    ans += a_cnd * (n - c_cnd)
print(ans)
        
        
        
    
    