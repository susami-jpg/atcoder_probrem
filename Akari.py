# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:48:21 2021

@author: kazuk
"""

#from sys import stdin
#input = stdin.readline
h, w, n, m = map(int, input().split())
maze = [[-1] + [0] * (w) + [-1] for _ in range(h)]
maze.insert(0, [-1] * (w + 2))
maze.append([-1] * (w + 2))
akari = [[0] * (w + 2) for _ in range(h + 2)]

for _ in range(n):
    a, b = map(int, input().split())
    maze[a][b] = 1

for _ in range(m):
    c, d = map(int, input().split())
    maze[c][d] = -1

def check_light(maze):
    hm = len(maze)
    wm = len(maze[0])
    for i in range(1, hm):
        block = 0
        light = False
        for j in range(1, wm):
            if maze[i][j] == -1:
                if light:
                    for k in range(block + 1, j):
                        akari[i][k] = 1
                block = j
                light = False
            if maze[i][j] == 1:
                light = True
    

def tench(maze):
    return [list(x) for x in zip(*maze)]

check_light(maze)

maze = tench(maze)
akari = tench(akari)

check_light(maze)

ans = 0
for i in akari:
    ans += sum(i)
print(ans)

            
                
            