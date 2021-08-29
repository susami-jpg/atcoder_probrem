# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:33:52 2021

@author: kazuk
"""

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

#ある集合mskの得点をO(1)で取得できるように前計算を行っておく
cst = [0] * (1 << n)
for msk in range(1 << n):
    point = 0
    group = []
    for j in range(n):
        if (msk >> j) & 1:
            group.append(j)
    for a in range(len(group)-1):
        for b in range(a + 1, len(group)):
            point += A[group[a]][group[b]]
    cst[msk] = point
    
#dp[msk]: グループが決まったうさぎがmskである場合の点数の最大値
#dp[msk]を確定させたいときに、mskの部分集合msk2を列挙する方法がある。
#msk2 ⊂ mskとすると、dp[msk] = dp[msk - msk2] + msk2のグループを作る事による点数
#つまり、もともとmsk-msk2がグループが決まっているときに、msk2グループを作ることを行う。
dp = [0] * (1 << n)

for msk in range(1, 1 << n):
    # 集合Mの部分集合を列挙
    v = (-1) & msk
    while v:
        msk2 = v
        dp[msk] = max(dp[msk], dp[msk^msk2] + cst[msk2])
        v = (v - 1) & msk

print(dp[-1])
