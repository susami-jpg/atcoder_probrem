# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:24:41 2021

@author: kazuk
"""

from itertools import accumulate
dista = [0, 0, 3, 5, 2, 3, 4, 3, 4, 2, 2, 3, 6, 2]
distb = [0, 0, 4, 3, 3, 2, 3]

dista = list(accumulate(dista))
distb = list(accumulate(distb))

trainA1_A7 = []
i = 0
while 1:
    time = 355 + 10 * i
    if time < 1380:
        trainA1_A7.append(time)
        i += 1
    else:
        break

trainA1_A13 = []
i = 0
while 1:
    time = 360 + 10 * i
    if time < 1380:
        trainA1_A13.append(time)
        i += 1
    else:
        break

trainA7_A1 = []
time = 366
for i in range(len(trainA1_A7)-1):
    trainA7_A1.append(time)
    time += 10

trainA7_A13 = [370]

trainA13_A1 = []
trainA13_A7 = []
i = 0
while 1:
    time = 352 + 10 * i
    if time < 1380:
        trainA13_A1.append(time)
        i += 1
    else:
        trainA13_A7.append(trainA13_A1.pop())
        break

trainB1_A7 = []
i = 0
while 1:
    time = 360 + 6 * i
    if time < 1380:
        trainB1_A7.append(time)
        i += 1
    else:
        break

trainA7_B1 = [371]
for i in trainB1_A7:
    trainA7_B1.append(i + 17)
trainA7_B1.pop()
    


def lineAup(s, hh):
    ans = []
    if s < 7:
        for t in trainA1_A7:
            time = t + (dista[s] - dista[1])
            if time // 60 == hh:
                ans.append(time % 60)
            if time // 60 > hh:
                break
    if s >= 7:
        for t in trainA7_A13:
            time = t + (dista[s] - dista[7])
            if time // 60 == hh:
                ans.append(time % 60)
            if time // 60 > hh:
                break
    for t in trainA1_A13:
        time = t + (dista[s] - dista[1])
        if time // 60 == hh:
            ans.append(time % 60)
        if time // 60 > hh:
            break
    ans.sort()
    hh = str(hh)
    if len(hh) == 1:
        hh = "0" + hh
    ans = ["0" + str(i) if len(str(i)) == 1 else str(i) for i in ans]
    if len(ans):
        print(hh +":", *ans)
    else:
        print("No train")

def lineAdown(s, hh):
    ans = []
    if s <= 7:
        for t in trainA7_A1:
            time = t + (dista[7] - dista[s])
            if time // 60 == hh:
                ans.append(time % 60)
            if time // 60 > hh:
                break
    if s > 7:
        for t in trainA13_A7:
            time = t + (dista[13] - dista[s])
            if time // 60 == hh:
                ans.append(time % 60)
            if time // 60 > hh:
                break
    for t in trainA13_A1:
        time = t + (dista[13] - dista[s])
        if time // 60 == hh:
            ans.append(time % 60)
        if time // 60 > hh:
            break
    ans.sort()
    ans = ["0" + str(i) if len(str(i)) == 1 else str(i) for i in ans]
    hh = str(hh)
    if len(hh) == 1:
        hh = "0" + hh
    if len(ans):
        print(str(hh)+":", *ans)
    else:
        print("No train")


def lineBup(s, hh):
    ans = []
    for t in trainB1_A7:
        time = t + (distb[s] - distb[1])
        if time // 60 == hh:
            ans.append(time % 60)
        if time // 60 > hh:
            break
    ans.sort()
    ans = ["0" + str(i) if len(str(i)) == 1 else str(i) for i in ans]
    hh = str(hh)
    if len(hh) == 1:
        hh = "0" + hh
    if len(ans):
        print(str(hh)+":", *ans)
    else:
        print("No train")

def lineBdown(s, hh):
    ans = []
    for t in trainA7_B1:
        time = t + (distb[6] - distb[s])
        if time // 60 == hh:
            ans.append(time % 60)
        if time // 60 > hh:
            break
    ans.sort()
    ans = ["0" + str(i) if len(str(i)) == 1 else str(i) for i in ans]
    hh = str(hh)
    if len(hh) == 1:
        hh = "0" + hh
    if len(ans):
        print(str(hh)+":", *ans)
    else:
        print("No train")

R, S, DIR, HH = input().split()
if R == "A":
    if len(S) == 3:
        S = S[1] + S[2]
    else:
        S = S[1]
    if DIR == "U":
        lineAup(int(S), int(HH))
    else:
        lineAdown(int(S), int(HH))
else:
    if S == "A7":
        s = 6
    elif len(S) == 3:
        s = int(S[1] + S[2])
    else:
        s = int(S[1])
    if DIR == "U":
        lineBup(s, int(HH))
    else:
        lineBdown(s, int(HH))

