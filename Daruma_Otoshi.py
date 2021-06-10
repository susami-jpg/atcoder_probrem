# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:02:15 2021

@author: kazuk
"""
ans = []
while True:
    try:
        n = int(input())
        if n == 0:
            break
        w = list(map(int, input().split()))
        
        dp = [[0] * n for _ in range(n)]
        
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                if l % 2 == 0:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                else:
                    if dp[i + 1][j - 1] == l - 1:
                        if abs(w[i] - w[j]) <= 1:
                            dp[i][j] = l + 1
                        else:
                            dp[i][j] = l - 1
                    for k in range(i + 1, j):
                        new = dp[i][k] + dp[k + 1][j]
                        if new > dp[i][j]:
                            dp[i][j] = new
        
        ans.append(dp[0][-1])
        #listA=list(map(int,input().split()))
        #listA<-[1,2,2,3,1]
        #ここに逐次処理を書けばいいと思う。
    except:
        break;
        #または、quit(),os.exit()をして止める。
for i in ans:
    print(i)
