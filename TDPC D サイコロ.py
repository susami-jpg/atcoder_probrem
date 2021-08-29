# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:27:04 2021

@author: kazuk
"""

from sys import exit
n, d = map(int, input().split())

a = 0
b = 0
c = 0
while d%2 == 0:
    d //= 2
    a += 1
while d%3 == 0:
    d //= 3
    b += 1
while d%5 == 0:
    d //= 5
    c += 1

if d != 1:
    print(0)
    exit()

dp = [[[[0] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)] for _ in range(n + 1)]
dp[0][0][0][0] = 1

# サイコロの目1~6を素因数分解
d2 = [0, 1, 0, 2, 0, 1]
d3 = [0, 0, 1, 0, 0, 1]
d5 = [0, 0, 0, 0, 1, 0]

#配るdp
for i in range(n):
    for j in range(a+1):
        for k in range(b+1):
            for l in range(c+1):
                #どの目が出るか
                #j,k,lがa,b,cを超えた場合はまとめて集約する(minをとってる)
                #j,k,lがDの素因数の指数部分より大きい場合は Dの指数部分の大きさに合わせることで, Dの倍数の確率も合わせて見ることが出来る.
                for m in range(6):
                    nc2 = min(j+d2[m], a)
                    nc3 = min(k+d3[m], b)
                    nc5 = min(l+d5[m], c)
                    dp[i+1][nc2][nc3][nc5] += dp[i][j][k][l]


print(dp[-1][a][b][c]/pow(6, n))


#もらうdp_ver(普通にやるとTLE)
#添え字(j,k,lに制限を付ける(10**8を超えるものは無視)しても間に合わず)
from sys import exit
n, d = map(int, input().split())
 
a = 0
b = 0
c = 0
while d%2 == 0:
    d //= 2
    a += 1
while d%3 == 0:
    d //= 3
    b += 1
while d%5 == 0:
    d //= 5
    c += 1
 
if d != 1:
    print(0)
    exit()
 
dp = [[[[0] * 27 for _ in range(40)] for _ in range(61)] for _ in range(n + 1)]
dp[0][0][0][0] = 1
ans = 0
for i in range(1, n+1):
    for j in range(61):
        #2**60は19桁
        for k in range(40):
            #3**40は20桁
            for l in range(27):
                #5**26は19桁
                dp[i][j][k][l] += dp[i-1][j][k][l]
                if j >= 1:
                    dp[i][j][k][l] += dp[i-1][j-1][k][l]
                if j >= 2:
                    dp[i][j][k][l] += dp[i-1][j-2][k][l]
                if k >= 1:
                    dp[i][j][k][l] += dp[i-1][j][k-1][l]
                if l >= 1:
                    dp[i][j][k][l] += dp[i-1][j][k][l-1]
                if j >= 1 and k >= 1:
                    dp[i][j][k][l] += dp[i-1][j-1][k-1][l]

for j in range(a, 61):
    for k in range(b, 40):
        for l in range(c, 27):
            ans += dp[-1][j][k][l]
 
 
print(ans/pow(6, n))
