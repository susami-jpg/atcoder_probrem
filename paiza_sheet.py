# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:12:59 2021

@author: kazuk
"""

n, m, s = map(int, input().split())
floor = []
color = [[] for _ in range(s + 1)]
for i in range(n):
    inp = list(str(input()))
    for k, j in enumerate(inp):
        if j != ".":
            if not color[int(j)]:
                color[int(j)].append((i, k))
                dy, dx = i, k
    floor.append(inp)
        

dxdy = [i for i in range(-m+1, 1, 1)]
def is_ok(c, y, x):
    for i in dxdy:
        for j in dxdy:
            sy = y + i
            sx = x + j
            if 0 > sy or 0 > sx:
                continue
            if sy + (m-1) > n-1 or sx + (m-1) > n-1:
                continue
            check = {str(c), "0"}
            for i in range(n):
                if sy <= i <= sy+m-1:
                    cnd = set(floor[i][sx:sx+m])
                    cnd_a1 = set(floor[i][0:sx])
                    if sx + m <= n-1:
                        cnd_a2 = set(floor[i][sx+m:])
                    else:
                        cnd_a2 = set()
                    if (not(cnd <= check)) or str(c) in cnd_a1 or str(c) in cnd_a2:
                        break
                else:
                    cnd = set(floor[i])
                    if str(c) in cnd:
                        break
            else:
                return (sy, sx)
            

def chenge(c, floor):
    newfloor = []
    for row in floor:
        row = "".join(row).replace(str(c), "0")
        newfloor.append(list(row))
    return newfloor

for i in range(s + 1):
    if len(color[i]) == 0:
        color[i].append((dy, dx))

ans = []
seen = [0] * (s + 1)
while len(ans) < s:
    for i in range(1, s+1):
        if seen[i]:
            continue
        sy, sx = color[i][0]
        cnd = is_ok(i, sy, sx)
        if cnd == None:
            continue
        sy, sx = cnd
        ans.append((i, sx+1, sy+1))
        floor = chenge(i, floor)
        seen[i] = 1
        
for i in range(s-1, -1, -1):
    print(*ans[i])


        
        
    
    
                    
                
                
                
            
    
    
        
        
    