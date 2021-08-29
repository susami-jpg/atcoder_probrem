# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 00:20:46 2021

@author: kazuk
"""

n, k = map(int, input().split())
p = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

seen = [False] * (n+1)
ans = None

for i in range(1, n+1):
    #すでに見ていればcontinue
    if seen[i]:continue
    #loopは始点iからはじまり、iに戻ってくるループを順番にリストで格納
    loop = [i]
    now = p[i]
    while now != i:
        loop.append(now)
        now = p[now]
    #lはloop一周の長さ
    l = len(loop)
    #Sはloopの和(一周した時に得られるpoint)
    S = sum(c[v] for v in loop)
    
    #loopの長さが1の場合
    if l == 1:
        seen[loop[0]] = True
        max_cost = max(S, S * k)
        if not ans:ans = max_cost
        else:ans = max(ans, max_cost)
    
    #ひとつのループ内で得られるポイントを全探索
    #始点を固定
    else:
        for a_ind in range(l):
            a = loop[a_ind]
            #ループ内の始点として確認したなら以降は確認する必要はない
            seen[a] = True
            dist_ab = 0
            cost_ab = 0
            #終点を固定
            for b_ind in range(a_ind+1, l + a_ind):
                b = loop[b_ind%l]
                #ab間の距離を更新
                dist_ab += 1
                #ab間のcostを更新
                cost_ab += c[b]
                #dist_abがk回以上ならそこにたどり着けないので探索終了
                if dist_ab > k:break
                #Sは負の場合もあるのでその場合0としてよい
                #何回回れるかは(k-dist_ab)回をループの長さで割ったfloor
                #最後の一周分のab間のcostをcost_abで足す
                max_cost = max(S, 0) * ((k-dist_ab)//l) + cost_ab
                if not ans:ans = max_cost
                else:ans = max(ans, max_cost)
            
print(ans)
         
    