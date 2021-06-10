# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:43:19 2021

@author: kazuk
"""
d = int(input())
n = int(input())
m = int(input())
tempo = [0, d]
house = []
for _ in range(n - 1):
    tempo.append(int(input()))
tempo = sorted(tempo)

def mindsearch(tempo, k):
    left = 0
    right = len(tempo)
    minl = d
    while left + 1 < right:
        mid = (left + right) // 2
        if tempo[mid] == k:
            minl = 0
            break
        if tempo[mid] < k:
            left = mid
        if tempo[mid] > k:
            right = mid
    minl = min(minl, abs(tempo[left] - k), abs(tempo[right] - k))
    return minl
#キャパオーバー
#s = 0
#for _ in range(m):
    #k = int(input())
    #s += mindsearch(tempo, k)

#print(s)

#bisectを使う場合
s = 0
import bisect
for _ in range(m):
    k = int(input())
    index = bisect.bisect(tempo, k)
    s += min(abs(tempo[index - 1] - k), abs(tempo[index] - k))
print(s)