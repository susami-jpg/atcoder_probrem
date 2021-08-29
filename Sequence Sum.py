# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:23:12 2021

@author: kazuk
"""

n, x, m = map(int, input().split())
mod_rec = [0] * m
mod_rec[x] = 1

def f(a):
    return pow(a, 2) % m

flg = 0
loop = [x]
now = x
cnt = 1
while 1:
    if cnt == n:
        break
    cnt += 1
    nex = f(now)
    if mod_rec[nex] == 1:
        ls = nex
        flg = 1
        break
    mod_rec[nex] = 1
    loop.append(nex)
    now = nex

if flg:
    ls_ind = loop.index(ls)
    L = len(loop[ls_ind:])
    L_prev = len(loop[:ls_ind])
    loop = loop[ls_ind:]
    
    K = (n - L_prev) // L
    K_mod = (n - L_prev) % L
    
    for a in loop:
        mod_rec[a] += K-1
    for i in range(K_mod):
        mod_rec[loop[i]] += 1

ans = 0
for i, count in enumerate(mod_rec):
    ans += i * count

print(ans)

        


    
    
    
