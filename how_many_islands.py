# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:27:46 2021

@author: kazuk
"""

w, h = map(int, input().split())

chart = [[-1 for _ in range(w + 2)]]
for _ in range(h):
    wt = [-1] + list(map(int, input().split())) + [-1]
    chart.append(wt)
chart.append([-1 for _ in range(w + 2)])

visited = []
chart_cnd = [-1] + [0 for _ in range(w)] + [-1]
sea = [-1 for _ in range(w + 2)]
visited.append(sea)
for _ in range(h):
    cc = chart_cnd[:] #コピーはこのようにしないと全てに変更が反映されてしまう
    visited.append(cc)
visited.append(sea)

stack = []
count = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        #すでに訪れていたら探索しない
        if visited[i][j] == 1:
            continue
        c = chart[i][j]
        visited[i][j] = 1 #訪れた場所として記録
        #海の場合
        if c == 0:
            continue
        #陸の場合
        stack.append([i, j])
        count += 1
        while stack:
            now = stack[-1] #現在地の更新
            a = now[0]
            b = now[1]
            #現在地の周りに陸地があるかどうか探索
            t = 0
            for n in range(-1, 2):
                for m in range(-1, 2):
                    x = a + n
                    y = b + m
                     #訪れていない場所なら更新
                    if visited[x][y] == 0:
                        visited[x][y] = 1
                        #陸ならばスタックに追加
                        if chart[x][y] == 1:
                            stack.append([x, y])
                            t += 1
            #探索結果全て行き止まりなら
            if t == 0:
                stack.pop()
print(count)
