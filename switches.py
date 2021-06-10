# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:50:32 2021

@author: kazuk
"""
N, M = map(int, input().split())
light = []
for _ in range(M):
    light.append(list(map(int, input().split())))
p = list(map(int, input().split()))

count = 0 #全ての電球が点灯するようなスイッチの on/off の状態の組み合わせの個数のカウント
for i in range(2 ** N): #10個のスイッチの準備
    light_on = 0 #いくつの電球がついているかをカウント
    for lnum, l in enumerate(light):
        switch = 0 #いくつのスイッチがonになっているかをカウント
        for j in range(1, len(l)):
            if ((i >> l[j] - 1) & 1): #iを二進数に変更し、電球ごとに存在するスイッチのon/offを確認
            #swichのon/offの状態は2進数で表され、スイッチは桁数と1個ずつずれているのでl[j] - 1とした
                switch += 1
        if switch % 2 == p[lnum]:
            light_on += 1 #電球の点灯確認
    if light_on == M: #全ての電球が点灯しているかの確認
        count += 1

print(count)



               
    
    
    