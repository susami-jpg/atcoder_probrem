# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:26:24 2021

@author: kazuk
"""
# i < j
# j - i = Ai + Aj を満たす(i, j)の組を見つける
#移行すると
# j - Aj = i + Ai
#　ここでjを固定するとidがj未満のidの人で i+Aiがj-Ajと等しい人の数を見ればいいことが分かる
#　今まで見てきた人のi+Aiをdictで持っておけばO(1)で上記の情報が得られる

from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
rec = defaultdict(int)

ans = 0
for i in range(n):
    x = i - A[i]
    y = i + A[i]
    ans += rec[x]
    rec[y] += 1

print(ans)
