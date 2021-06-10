# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:53:13 2021

@author: kazuk
"""

while True:
    h = int(input())
    if h == 0:
        break
    banmen = []
    for _ in range(h):
        banmen.append(list(map(int, input().split())) + [0])
    
    ans = 0
    def search(banmen):
        global ans
        oldans = ans
        for i in range(h):
            cnt = 1
            oldj = 0
            for j in range(1, 6):
                if banmen[i][j] == -1:
                    oldj = j
                    cnt = 1
                    continue
                if banmen[i][j] == banmen[i][oldj]:
                    cnt += 1
                    lastj = j
                else:
                    if cnt >= 3:
                        ans += cnt * banmen[i][oldj]
                        for k in range(oldj, lastj + 1):
                            banmen[i][k] = -1
                    oldj = j
                    cnt = 1
        if oldans == ans:
            return False
        else:
            return banmen
    
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
            
    while True:
        banmen = search(banmen)
        if banmen == False:
            print(ans)
            break
        banmen = newboard(banmen)

                
            