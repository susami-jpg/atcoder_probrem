# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:27:23 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
bporn = []
for _ in range(m):
    x, y = map(int, input().split())
    bporn.append((x, y))
bporn.sort()
current = 0
ans = set()
add_set = set()
del_set = set()
ans.add(n)

for x, y in bporn:
    #階層が違うならばansを更新
    if x != current:
        current = x
        for i in del_set:
            ans.remove(i)
        for i in add_set:
            ans.add(i)
        add_set = set()
        del_set = set()
    
    #階層が同じ限りansから削除する要素と足す要素を保持しておく
    if y in ans:
        del_set.add(y)
    if y-1 in ans or y+1 in ans:
        add_set.add(y)

#最後の階層での更新はないので更新
ans = (ans - del_set) | add_set
print(len(ans))
    
  
        
        
    