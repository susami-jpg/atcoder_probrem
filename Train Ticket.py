# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:18:25 2021

@author: kazuk
"""

s = list(map(int, list(input())))
ans = 0
for i in range(1 << 3):
    ans = [str(s[0])]
    cnd = s[0]
    now = 1
    for j in range(3):
        if (i >> j) & 1:
            cnd += s[now]
            ans.append("+")
        else:
            cnd -= s[now]
            ans.append("-")
        ans.append(str(s[now]))
        now += 1
    if cnd == 7:
        ans.append("=")
        ans.append("7")
        print("".join(ans))
        break

     
        
