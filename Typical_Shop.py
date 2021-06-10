# -*- coding: utf-8 -*-
"""
Created on Thu May 27 22:22:36 2021

@author: kazuk
"""

#想定解法だがTLE
#一応2**nの解法があるそう
from bisect import bisect_left, bisect_right
n, k, p = map(int, input().split())
a = list(map(int, input().split()))

s1 = a[:n//2]
s2 = a[n//2:]

#選んだ荷物の個数ごとにできる可能性のある価値の大きさを記録
s1v = [[] for _ in range(len(s1) + 1)]
s2v = [[] for _ in range(len(s2) + 1)]

#半分全列挙
for i in range(1 << len(s1)):
    vcnd = 0
    cnt = 0
    for j in range(len(s1)):
        if (i >> j) & 1:
            vcnd += s1[j]
            cnt += 1
    #選んだ荷物個数ごとの価値のリストを昇順に保つ
    ind = bisect_left(s1v[cnt], vcnd)
    s1v[cnt].insert(ind, vcnd)


for i in range(1 << len(s2)):
    vcnd = 0
    cnt = 0
    for j in range(len(s2)):
        if (i >> j) & 1:
            vcnd += s2[j]
            cnt += 1
    ind = bisect_left(s2v[cnt], vcnd)
    s2v[cnt].insert(ind, vcnd)

ans = 0
for cnt in range(len(s1) + 1):
    vcnd = s1v[cnt]
    vcnd2 = s2v[k-cnt]
    for v in vcnd:
        ans += bisect_right(vcnd2, p - v)

print(ans)
        


            
            
