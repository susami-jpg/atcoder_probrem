# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 12:48:47 2021

@author: kazuk
"""



import heapq
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
 
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
 
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
 
    def top(self):
        return self.hq[0] * self.sign


"""
初期化
q = Heapq(arr, desc) のように書けばいいです

第1引数 arr は初期化に使う配列です 空っぽから始める場合は []でいいです
第2引数 desc は大きい順に取り出すなら True、小さい順ならFalse です。Falseは省略可です。
pop()
q.pop() のようにすると値が返ります
一番小さいの or 一番大きいのを集合から取り出します。
初期化時 desc=Trueを指定していたなら大きい方が出てきます。
取り出された要素は集合から消えます。

push()
q.push(a) のようにすると集合に aを追加します

top()
q.top() のようにすると値が返ります
一番小さいの or 一番大きいのを参照できます
初期化時 desc=Trueを指定していたなら大きい方が出てきます。
pop()に似てますが、参照するだけで、集合から値が消えることはありません。
O(1)でめっちゃ速いです
"""

n = int(input())
a = list(map(int, input().split()))
INF = 10**15
#dp1[i]: a[:i]の中からn個選んでできる総和の最大値
#dp2[i]:a[i:]の中からn個選んでできる総和の最小値
#iはn~2n-1まで動く(-nしてdpテーブルに記録)
dp1 = [0] * (n+1)
dp2 = [INF] * (n+1)
S1 = sum(a[:n])
S2 = sum(a[2*n:])
dp1_q = Heapq(a[:n], False)
dp2_q = Heapq(a[2*n:], True)
dp1[0] = S1
dp2[-1] = S2

#dp1
for i in range(1, n+1):
    min_a = dp1_q.top()
    if a[n-1+i] > min_a:
        S1 -= min_a
        dp1_q.pop()
        S1 += a[n-1+i]
        dp1_q.push(a[n-1+i])
        dp1[i] = S1
    else:
        dp1[i] = dp1[i-1]
        
#dp2
for i in reversed(range(n)):
    max_a = dp2_q.top()
    if a[n+i] < max_a:
        S2 -= max_a
        dp2_q.pop()
        S2 += a[n+i]
        dp2_q.push(a[n+i])
        dp2[i] = S2
    else:
        dp2[i] = dp2[i-1]

ans = -INF
for i in range(n+1):
    cnd = dp1[i] - dp2[i]
    ans = max(ans, cnd)
print(ans)

    
    

        
    
    



