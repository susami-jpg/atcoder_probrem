# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 19:51:45 2021

@author: kazuk
"""

import math
from sys import exit
n, m = map(int, input().split())
A = list(map(int,input().split()))

# 2で割ったものに置き換え
# X=ak×(p+0.5) →　X=a′k×(2p+1)
A = [i // 2 for i in A]

#inputされた配列Aの要素が2で何回割れるかを確認
#全ての要素の2で割れる回数が同じであればok、それ以外は0
def two(n):
    cnt = 0
    while True:
        if n % 2 == 1:
            return n, cnt
        else:
            n = n // 2
            cnt += 1
a = []
divcnt = None
for i in A:
    n, cnt = two(i)
    if divcnt == None:
        divcnt = cnt
    else:
        if divcnt != cnt:
            print(0)
            exit()
            
#配列Aの最小公倍数を求める
x=1
for i in A:
    x=i*x//math.gcd(i,x)

#mまでに存在するxの公倍数の個数が答えになる(奇数倍しかとらないことに注意：a' * (2*p + 1)より)
t = m // x
ans = t / 2
print(math.ceil(ans))
    
    
