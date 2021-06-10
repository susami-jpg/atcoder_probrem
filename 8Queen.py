# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:35:34 2021

@author: kazuk
"""
import numpy as np
from itertools import permutations


k = int(input())
chess = [[0] * 8 for _ in range(8)]
rc = []
for _ in range(k):
    r, c = map(int, input().split())
    rc.append((r, c))

#斜めの被り判定
def judge(chess):
    for i in range(8):
        chessr = np.fliplr(chess) #fliplr() の効果: 配列を左右反転させる
        p1 = sum(np.diag(chess, k = i))
        p2 = sum(np.diag(chess, k = -i))
        p3 = sum(np.diag(chessr, k = i))
        p4 = sum(np.diag(chessr, k = -i))
        plist = [p1, p2, p3, p4]
        if not all([j <= 1 for j in plist]):
            return False
    else:
        return True

    
#順列によって8角クイーンの配置のすべてのパターンを網羅
#縦横が被った時点でoutなので順列によって候補を絞れる
#[3,1,2,5,4,7,6,0]なら0行目3列目にQ、1行目1列目にQ、2行目2列目にQ、3行目5列目にQ,,,と決まる
for perm in permutations(range(8)): #条件の位置にQがあるかの確認　なければその組み合わせを調べる必要はない
    for (r, c) in rc:
        if perm[r] != c:
            break
    else:
        chess_copy = np.array(chess[:]) #チェス盤準備
        for x, y in enumerate(perm): #Qの配置
            chess_copy[x][y] = 1
        if judge(chess_copy):
            for t in perm:
                s = ['.'] * 8
                s[t] = 'Q'
                print(''.join(s))
            break
                    

    
      
    




