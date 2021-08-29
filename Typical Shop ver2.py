# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:37:09 2021

@author: kazuk
"""

from collections import defaultdict
from bisect import bisect_right
n, k, p = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[:n//2]
A2 = A[n//2:]

def harf_comb(a):
    rec = defaultdict(list)
    N = len(a)
    for i in range(1 << N):
        cnt = 0
        price = 0
        for j in range(N):
            if (i >> j) & 1:
                cnt += 1
                price += a[j]
        #ここでinsort_leftをやるとTLE
        #O(2**(n//2) * logS(Sは各recの要素数))　定数倍が重い?(Sは最悪40Cxの最大値)
        #あとでまとめてsortするとAC
        #O(n**2 logn)　今回はnが小さいのでまとめてソートしたほうが早い(ソートはnlogn)?
        rec[cnt].append(price)
    return rec

def OrLessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

A1_rec = harf_comb(A1)
A2_rec = harf_comb(A2)
for i in range(max(len(A1), len(A2))):
    A1_rec[i].sort()
    A2_rec[i].sort()
    

ans = 0
for i in range(min(k+1, n//2+1)):
    rest = k - i
    for p_half in A1_rec[i]:
        p_rest = p - p_half
        cnd, _ = OrLessThan(p_rest, A2_rec[rest])
        ans += cnd

print(ans)

        


    
                
        
