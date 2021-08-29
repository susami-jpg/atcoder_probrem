# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 01:02:37 2021

@author: kazuk
"""

n, m = map(int, input().split())
kill_a = list(map(int, input().split()))
kill_b = list(map(int, input().split()))
mod = 10**9+7

def part_num(n, k):
    if n == k == 0:
        return 1
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for j in range(1, k+1):
        dp[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i - j >= 0:
                dp[i][j] = (dp[i][j-1] + dp[i-j][j])%mod
            else:
                dp[i][j] = dp[i][j-1]
                
    return dp

def death_comb(n, kill, death):
    mod = 10**9 + 7
    kill_S = sum(death)
    group = [1]
    for i in range(1, len(kill)):
        if kill[i] == kill[i-1]:
            group[-1] += 1
        else:
            group.append(1)
    
    #分割数をO(1)で得るための前処理
    max_group = max(group)
    P = part_num(kill_S, max_group)
    
    #デス数の総和は相手のキル数の総和と等しい
    #キル数が同じ区間ではデス数は広義単調増加する
    #キル数が同じプレイヤーを1つのグループにまとめる。
    #「dp[g][sm] := g番目のグループまででデス数がsmである組み合わせ数」これを求める。
    #dp[g + 1][sm + i] += dp[g][sm] * (g+1番目のグループでデス数の総和がiとなる組み合わせ数)
    #で更新できるため、「(g+1番目のグループでデス数の総和がiとなる組み合わせ数)」を考えてみよう。
    #これは丁度分割数の応用で計算ができる。
        
    dp = [[0] * (kill_S + 1) for _ in range(len(group))]
    for sm in range(kill_S + 1):
        dp[0][sm] = P[sm][group[0]]
        
    for g in range(len(group)-1):
        for sm in range(kill_S + 1):
            for i in range(kill_S + 1 - sm):
                if sm+i > kill_S:continue
                cnd = P[i][group[g+1]]
                dp[g+1][sm+i] += (dp[g][sm] * cnd)%mod
    return dp[-1][kill_S]

ans = death_comb(n, kill_a, kill_b) * death_comb(m, kill_b, kill_a) 
print(ans%mod)

                
    
    