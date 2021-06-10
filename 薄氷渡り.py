# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:24:11 2021

@author: kazuk
"""
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(int(1E+7))
m = int(input())
n = int(input())
chart = []
sea = [0] * (m + 2)
chart.append(sea)
for _ in range(n):
    ch = [0] + list(map(int, input().split())) + [0]
    chart.append(ch)
chart.append(sea)

dig = [(1, 0), (0, 1), (-1, 0), (0, -1)]

ans = 0
#dfsは現在地(n,m)と深さdを受け取り、深さ優先探索を行う関数
def dfs(n, m, d):
    if chart[n][m] == 0:
        return
    global ans
    if ans < d:
        ans = d #深さの更新
    chart[n][m] = 0 #氷を割ることによって後戻りできないようにする
    for a, b in dig:
        x = n + a
        y = m + b
        dfs(x, y, d + 1)
    chart[n][m] = 1 #再帰による探索が終了したら氷を元に戻す

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dfs(i, j, 1)

print(ans)


#maxlen = 0

#関数dfsは頂点uを受け取り、そこから行ける最大距離を返す関数
#stack = []
#def dfs(a, b):
 #   t = 0
  #  u = (a, b)
   # stack.append(u)
    #visited.add(u)
    #global maxlen
    #maxlen = max(maxlen, len(stack))
    #while stack:
    #    now = stack[-1]
     #   for (i, j) in dig:
      #      x = now[0] + i
       #     y = now[1] + j
        #    if (x, y) not in visited:   
         #       if chart[x][y] == 1:
          #          t += 1
           #         dfs(x, y)
        #if t == 0:
         #   stack.pop()

#for a in range(1, n + 1):
 #   for b in range(1, m + 1):
  #      if chart[a][b] == 0:
   #         continue
    #    visited = set()
     #   dfs(a, b)

#print(maxlen)



    
    

            