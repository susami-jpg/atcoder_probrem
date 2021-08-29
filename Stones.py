# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:34:26 2021

@author: kazuk
"""

n, k = map(int, input().split())
A = list(map(int, input().split()))

#dp[i][j]: 石がi個の時にjがA個石をとる行動をとった時の勝敗
dp = [[0] * 2 for _ in range(k + 1)]
dp[0][0] = 1

for i in range(k+1):
    for j in range(2):
        turn = j
        #相手が勝つという初期化（i-a < 0なら相手の勝利だから)
        winner = j ^ 1
        #何個とるかを全探索
        #ひとつでも自分が勝てる選択肢があれば、自分の勝利
        for a in A:
            #ぴったりにとれるなら確実に勝てるのでwinnerを更新
            if i - a == 0:
                winner ^= 1
                break
            #i-aが正なら、残りの石がi-a個で相手のターンの時の結果を見る
            if i - a > 0:
                #自分が勝っていれば勝者は自分になるはずなのでwinnerを更新し、探索終了
                if dp[i-a][turn^1] == turn:
                    winner ^= 1
                    break
        dp[i][j] = winner
     
            
if dp[k][0] == 0:
    print("First")
else:
    print("Second")




