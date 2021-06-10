# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:38:34 2021

@author: kazuk
"""
inf = 10 ** 10
h, w = map(int, input().split())
maryoku = []
for _ in range(10):
    c = list(map(int, input().split()))
    maryoku.append(c)

for k in range(10):
    for i in range(10):
        for j in range(10):
            maryoku[i][j] = min(maryoku[i][j], maryoku[i][k] + maryoku[k][j])

ans = 0
for _ in range(h):
    c = list(map(int, input().split()))
    for i in c:
        if i == -1:
            continue
        else:
            ans += maryoku[i][1]
print(ans)
        

            
                
            
            
            

        
        
    
    