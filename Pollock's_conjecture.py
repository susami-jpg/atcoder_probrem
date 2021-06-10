# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:10:18 2021

@author: kazuk
"""
nlist = []
while True:
    try:
        nlist.append(int(input()))
        #listA=list(map(int,input().split()))
        #listA<-[1,2,2,3,1]
        #ここに逐次処理を書けばいいと思う。
    except:
        break;
        #または、quit(),os.exit()をして止める。

nmax = max(nlist)
dp = [10 ** 15] * (nmax + 1)
dp_odd = [10 ** 15] * (nmax + 1)
dp[0] = 0
dp_odd[0] = 0

def pol(n):
    return int(n * (n + 1) * (n + 2) / 6)

for i in range(1, nmax + 1):
    #変数iは何番目までの数字を使ってよいかを表す(dpのインデックスに相当)
    j = 1
    while pol(j) <= i:
        #変数jはi以下の数字でpolに代入するための変数
        dp[i] = min(dp[i], dp[i - pol(j)] + 1)
        j += 1
    k = 1
    while pol(k) <= i:
        if pol(k) % 2 == 1:
            dp_odd[i] = min(dp_odd[i], dp_odd[i - pol(k)] + 1)
        k += 1

for i in nlist:
    if i == 0:
        continue
    print(dp[i], dp_odd[i])
    
    
            
        
        
        
    
    
    