# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:28:45 2021

@author: kazuk
"""

from sys import exit
n = int(input())

for k in range(1, n + 1):
    e = k * (k + 1) // 2
    if e == n:
        element = k
        sn = k + 1
        break
else:
    print('No')
    exit()

print('Yes')
print(sn)
S = [[] for _ in range(sn)]

#とりあえず被らないように分配
elim = element
Si = 0
for i in range(1, n + 1):
    if len(S[Si]) == elim:
        elim -= 1
        Si += 1
    S[Si].append(i)

for i in range(sn - 1):
    now = i + 1
    for e in S[i][:len(S[i]) - i]:
        S[now].append(e)
        now += 1

for s in S:
    print(len(s),' '.join(map(str, s)))
    
#考え方や実装は以下を参照
#https://drken1215.hatenablog.com/entry/2018/10/29/004900
        
    

    
    
    