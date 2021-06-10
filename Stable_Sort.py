# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:35:37 2021

@author: kazuk
"""

def BubbleSort(C, n):
    flg = 1
    while flg:
        flg = 0
        for j in range(n - 1, 0, -1):
            if C[j - 1][1] > C[j][1]:
                C[j - 1], C[j] = C[j], C[j - 1]
                flg = 1
    return C

def SelectionSort(C, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if C[minj][1] > C[j][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def isStable(inp, out):
    for i in range(n - 1):
        for j in range(i + 1, n):
            for a in range(n - 1):
                for b in range(a + 1, n):
                    if inp[i][1] == inp[j][1] and inp[i] == out[b] and inp[j] == out[a]:
                        return False
    return True

def cardprint(card):
    ans = []
    for i in card:
        ans.append(i[0] + str(i[1]))
    print(*ans)

n = int(input())
c = list(map(str, input().split()))
card = []
for i in c:
    i = list(i)
    card.append((i[0], int(i[1])))
    
bubble = BubbleSort(card[:], n)
cardprint(bubble)
print("Stable")
select = SelectionSort(card[:], n)
cardprint(select)
if isStable(card, select):
    print("Stable")
else:
    print("Not stable")
    

