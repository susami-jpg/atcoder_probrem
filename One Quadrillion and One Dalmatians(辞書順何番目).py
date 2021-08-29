# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:04:30 2021

@author: kazuk
"""

n = int(input())
abc = [i for i in range(97, 123)]
#各ブロック(1桁の名前の数、2桁の名前の数、3桁の名前の数、、、)を計算し、累積和をとる
acc_26 = [0] * 16
for i in range(1, 16):
    acc_26[i] += pow(26, i) + acc_26[i-1]

for i in range(15):
    if acc_26[i] < n <= acc_26[i+1]:
        keta = i+1
        break

#桁数が分かったところで、そのブロックで何番目かを考える
#0indexで考えるために-1
n -= (acc_26[keta-1] + 1)

#あとはnについて26進数で復元
ans = []
for _ in range(keta):
    ans.append(chr(abc[n%26]))
    n //= 26

print("".join(ans[::-1]))


#そもそも入力されたnを26進数として変換して求めてもよい
from sys import setrecursionlimit
setrecursionlimit(10**7)
abc = [i for i in range(97, 123)]
n = int(input())
ans = []
def rec(n):
    #0indexでやる
    n -= 1
    ans.append(chr(abc[n%26]))
    if n < 26:
        return
    rec(n//26)


rec(n)
print("".join(ans[::-1]))



