# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 01:07:48 2021

@author: kazuk
"""

from sys import exit
s = list(input())
eight = []
for i in range(13, 125):
    e = str(8 * i)
    if "0" in e:
        continue
    eight.append(e)

if len(s) == 1:
    if int("".join(s)) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
elif len(s) == 2:
    s1 = int("".join(s))
    s2 = int("".join(s[1] + s[0]))
    if s1 % 8 == 0 or s2 % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
else:
    element = [0] * 10
    for i in s:
        element[int(i)] += 1
    for cnd in eight:
        if len(set(cnd)) == 1:
            if element[int(cnd[0])] >= 3:
                print("Yes")
                exit()
        elif len(set(cnd)) == 2:
            if cnd[0] == cnd[1]:
                if element[int(cnd[0])] >= 2 and element[int(cnd[2])]:
                    print("Yes")
                    exit()
            elif cnd[0] == cnd[2]:
                if element[int(cnd[0])] >= 2 and element[int(cnd[1])]:
                    print("Yes")
                    exit()
            else:
                if element[int(cnd[1])] >= 2 and element[int(cnd[0])]:
                    print("Yes")
                    exit()
        else:
            if element[int(cnd[0])] and element[int(cnd[1])] and element[int(cnd[2])]:
                print("Yes")
                exit()
    else:
        print("No")
        