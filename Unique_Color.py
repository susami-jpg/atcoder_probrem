# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:16:59 2021

@author: kazuk
"""
import sys
sys.setrecursionlimit(100000)
n = int(input())
c = list(map(int, input().split()))
st = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    st[a].append(b)
    st[b].append(a)

visited = 0
visited = [0] * (n + 1)
visited[0] = 1
color = [0] * (10 ** 6)
ans = []
count = 0
def dfs(s):
    global count
    if count == n:
        return
    global color
    visited[s] = 1
    count += 1
    if color[c[s - 1]] == 0:
        ans.append(s)
    color[c[s - 1]] += 1
    for i in st[s]:
        if visited[i] == 0:
            dfs(i)
    color[c[s - 1]] -= 1

  
dfs(1)
ans.sort()
for i in ans:
    print(i)
    

    
    



    


    