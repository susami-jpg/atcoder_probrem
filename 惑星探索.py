# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:49:53 2021

@author: kazuk
"""

m, n = map(int, input().split())
k = int(input())
town = [[[0, 0, 0] for _ in range(n + 1)]]
for _ in range(m):
    kukaku = [[0, 0, 0]]
    for i in list(input()):
        J = kukaku[-1][0]
        O = kukaku[-1][1]
        I = kukaku[-1][2]
        if i == 'J':
            kukaku.append([J+1, O, I])
        elif i == 'O':
            kukaku.append([J, O+1, I])
        else:
            kukaku.append([J, O, I+1])
    town.append(kukaku)

town_t = [list(x) for x in zip(*town)]
newtown_t = []
for kukaku in town_t:
    new = []
    for part in kukaku:
        if not new:
            new.append(part)
        else:
            J = new[-1][0]
            O = new[-1][1]
            I = new[-1][2]
            new.append([J+part[0], O+part[1], I+part[2]])
    newtown_t.append(new)

newtown = [list(x) for x in zip(*newtown_t)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    J = newtown[c][d][0] - newtown[a - 1][d][0] - newtown[c][b - 1][0] + newtown[a - 1][b - 1][0]
    O = newtown[c][d][1] - newtown[a - 1][d][1] - newtown[c][b - 1][1] + newtown[a - 1][b - 1][1]
    I = newtown[c][d][2] - newtown[a - 1][d][2] - newtown[c][b - 1][2] + newtown[a - 1][b - 1][2]
    print(J, O, I)
    
    