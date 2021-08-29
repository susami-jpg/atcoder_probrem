# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 00:57:14 2021

@author: kazuk
"""

from sys import exit

s = list(input())
t = list(input())
ls = len(s)
lt = len(t)
if lt > ls:
    print("UNRESTORABLE")
    exit()

def match(a, b):
    for i in range(len(a)):
        if a[i] != b[i] and a[i] != "?":
            return False
    else:
        return True

def check(a, b):
    for i in range(len(a)):
        if ord(a[i]) > ord(b[i]):
            return b
        elif ord(a[i]) < ord(b[i]):
            return a
    else:
        return a

ans = None
for i in range(ls-lt, -1, -1):
    if match(s[i:i+lt], t):
        cnd = s[:i] + t + s[i+lt:]
        cnd = "".join(cnd)
        cnd = cnd.replace("?", "a")
        if not ans:
            ans = cnd
        else:
            ans = check(ans, cnd)

if ans:
    print(ans)
else:
    print("UNRESTORABLE")