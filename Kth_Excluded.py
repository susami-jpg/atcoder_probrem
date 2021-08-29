# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:28:06 2021

@author: kazuk
"""

"""
s = input()
s = list(input())
n = int(input())
n, k = map(int, input().split())
a = list(map(int, input().split()))
"""

from itertools import accumulate
from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))
maxa = 10 ** 18
blank = []
prev = 0
for i in a:
    blank.append(i - prev - 1)
    prev = i
blank.append(maxa+1)
a = [0] + a
blank = [0] + list(accumulate(blank))

for _ in range(q):
    k = int(input())
    l = bisect_left(blank, k)
    if blank[l] >= k:
        cnt = blank[l-1]
    else:
        cnt = blank[l]
    ans = a[l-1] + (k - cnt)
    print(ans)
    


    
    