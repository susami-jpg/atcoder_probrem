# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:04:08 2021

@author: kazuk
"""
"""
#key昇順ソート
dct = { 2: 3, 3: 4, 1: 2, 0: 8, 4: 2 }
dct = sorted(dct.items())
print(dct)
#=> [(0, 8), (1, 2), (2, 3), (3, 4), (4, 2)]

dct = { 2: 3, 3: 4, 1: 2, 0: 8, 4: 2 }
for k, v in sorted(dct.items()):
    print(str(k) + ": " + str(v))
    

0: 8
1: 2
2: 3
3: 4
4: 2
"""

from collections import defaultdict

N, C = map(int, input().split())
#defaultdict(int)とすると辞書に初期値がない場合は、デフォルト値で初期化する
#defaultdictでできたのは辞書型ではなくタプルindex[0]がキーでindex[1]がvalue
event = defaultdict(int)
for _ in range(N):
    a, b, c = map(int, input().split())
    event[a] += c
    event[b+1] -= c

event = sorted(event.items())
event = dict(event)

#累積和をとりながら答え作製
ans = 0
past = 0
cost = 0
for k, v in event.items():
    ans += min(C, cost) * (k - past)
    past = k
    cost += v
print(ans)


#累積和をとる
prev = None
for key in event:
    if prev == None:
        prev = key
        continue
    event[key] += event[prev]
    prev = key
    
print(event)
    

ans = 0
past = None
for k, v in event.items():
    if past == None:
        past = k
        cost = v
        continue
    ans += min(cost, C) * (k-past)
    past = k
    cost = v

print(ans)


    


    
    


    
    
    
