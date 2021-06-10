# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:28:43 2021

@author: kazuk
"""

n = int(input())
ans=0
if n>=1000: ans+=n-999
if n>=1000000: ans+=n-999999
if n>=1000000000: ans+=n-999999999
if n>=1000000000000: ans+=n-999999999999
if n>=1000000000000000: ans+=n-999999999999999
print(ans)

    
    
