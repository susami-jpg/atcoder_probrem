# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:49:05 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a_rec = [0] * 46
b_rec = [0] * 46
c_rec = [0] * 46
for i in range(n):
    a_rec[a[i]%46] += 1
    b_rec[b[i]%46] += 1
    c_rec[c[i]%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46 == 0:
                ans += (a_rec[i] * b_rec[j] * c_rec[k])

print(ans)

        
