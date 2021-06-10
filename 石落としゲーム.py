# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:59:19 2021

@author: kazuk
"""

from copy import deepcopy
h, w, k = map(int, input().split())
banmen = []
for _ in range(h):
    banmen.append(list(map(int, list(str(input())))) + [0])

def search(banmen, t):
    global ans
    oldans = ans
    pa = 0
    for i in range(h):
        cnt = 1
        oldj = 0
        for j in range(1, w + 1):
            if banmen[i][j] == banmen[i][oldj]:
                cnt += 1
                lastj = j
            else:
                if cnt >= k and banmen[i][oldj] != -1:
                    pa += banmen[i][oldj] * cnt
                    for l in range(oldj, lastj + 1):
                        banmen[i][l] = -1
                cnt = 1
                oldj = j
    ans += 2 ** t * pa
    if oldans == ans:
        return False, t + 1
    else:
        return banmen, t + 1

def newboard(banmen):
    newbanmen_t = []
    banmen_t = [list(x) for x in zip(*banmen)]
    for col in banmen_t:
        minacnt = col.count(-1)
        newcol = [i for i in col if i != -1]
        newcol = [-1] * minacnt + newcol
        newbanmen_t.append(newcol)
    newbanmen = [list(x) for x in zip(*newbanmen_t)]
    return newbanmen

def delcell(i, j, banmen):
    banmen[i][j] = -1
    return banmen

ans_cnd = []
for a in range(h):
    for b in range(w):
        banmen_c = deepcopy(banmen)
        ans = 0
        t = 0
        banmen_n = delcell(a, b, banmen_c)
        banmen_n = newboard(banmen_n)
        while True:
            banmen_n, t = search(banmen_n, t)
            if banmen_n == False:
                ans_cnd.append(ans)
                break
            else:
                banmen_n = newboard(banmen_n)

print(max(ans_cnd))

                
            
        
    