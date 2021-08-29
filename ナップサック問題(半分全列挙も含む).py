# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:25:08 2021

@author: kazuk
"""

from bisect import bisect_right
from collections import defaultdict


def OrLessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

N, W = map(int, input().split())
S_v = 0
S_w = 0
ns = []
for _ in range(N):
    v, w = map(int, input().split())
    ns.append((v, w))
    S_v += v
    S_w += w

if N <= 30:
    A = ns[:N//2]
    B = ns[N//2:]
    A_vw = []
    B_vw = []
    A_w = []
    B_w = []
    nA = len(A)
    nB = len(B)
    for i in range(1 << nA):
        v_cnd, w_cnd = 0, 0
        for j in range(nA):
            if (i >> j) & 1:
                v, w = A[j]
                v_cnd += v
                w_cnd += w
        A_vw.append((w_cnd, v_cnd))
    for i in range(1 << nB):
        v_cnd, w_cnd = 0, 0
        for j in range(nB):
            if (i >> j) & 1:
                v, w = B[j]
                v_cnd += v
                w_cnd += w
        B_vw.append((w_cnd, v_cnd))
    max_v = -1
    S_A = defaultdict(int)
    A_vw.sort()
    for i in range(len(A_vw)):
        w, v = A_vw[i]
        if max_v < v:
            S_A[w] = max(v, S_A[w])
            A_w.append(w)
        max_v = max(max_v, v)
        
    max_v = -1
    S_B = defaultdict(int)
    B_vw.sort()
    for i in range(len(B_vw)):
        w, v = B_vw[i]
        if max_v < v:
            S_B[w] = max(v, S_B[w])
            B_w.append(w)
        max_v = max(max_v, v)
        
    
    ans = 0
    for i in range(len(A_w)):
        rest = W - A_w[i]
        if rest < 0:continue
        _, ind = OrLessThan(rest, B_w)
        cnd = S_A[A_w[i]] + S_B[B_w[ind]]
        ans = max(ans, cnd)
    print(ans)
    
elif S_v > S_w:
    dp = [[0] * (S_w + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(S_w):
            v, w = ns[i]
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+w <= S_w:
                dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v)
    print(dp[-1][W])

else:
    INF = 10**15
    dp = [[INF] * (S_v + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(S_v):
            v, w = ns[i]
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j+v <= S_v:
                dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j] + w)

    for v in range(S_v, -1, -1):
        if dp[-1][v] <= W:
            print(v)
            break
    