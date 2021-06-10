# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 22:22:59 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 15
if n == 1:
    print(a[0])
else:
    for i in range(2 ** (n - 1) + 1):
        before = 0
        now = 0
        s = []
        for j in range(n):
            now += 1
            if (i >> j) & 1:
                continue
            else:
                apart = a[before:now]
                before = now
                s1 = 0
                for ap in apart:
                    s1 = s1 | ap
                s.append(s1)
        s2 = None
        for sp in s:
            if s2 == None:
                s2 = sp
            else:
                s2 = s2 ^ sp
        if s2 < ans:
            ans = s2
    print(ans)
            
                
            
    








def split_list(l, n):
    """
    リストをサブリストに分割する
    :param l: リスト
    :param n: サブリストの要素数
    :return: 
    """
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]





        
        
 
