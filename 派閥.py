# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 01:20:43 2021

@author: kazuk
"""
from itertools import combinations
from sys import exit

N, M = map(int, input().split())
rel = [[0 for _ in range(N)] for _ in range(N)] #n * nの対人関係表
for _ in range(M):
    x, y = map(int, input().split())
    rel[x - 1][y - 1] = 1 #-1でインデックスにあわせる
    rel[y - 1][x - 1] = 1 #存在する関係を記録

for i in range(N, 1, -1): #N人の議員の派閥の大きさを決定、最大値を返すので大きいほうから
    for faction in combinations(range(N), i): #N人の中からi人を選出し、派閥を形成
        for comb in combinations(faction, 2): 
            #形成された派閥から二人組の組み合わせを一組ずつ見ていき、本当に存在する関係かを確認
            if rel[comb[0]][comb[1]] == 0:
                #もう一方の組み合わせ(rel[comb[1]][comb[0]]も同じ結果であるはずなので評価しなくてよい)
                break
            #関係がなければその時点で探索終了
        else:
            #ループが正常に終了すれば全ての関係が存在する
            print(i)
            exit()
        
print(1) #どの人間関係も存在しない場合           
    
    
   

    










