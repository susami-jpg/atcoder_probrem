# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:21:25 2021

@author: kazuk
"""


import numpy as np
def I(): return int(input())
def TI(): return list(map(int,input().split()))
n = I()
AB = np.array([TI() for _ in range(n)])
[Amin, Bmin] = np.min(AB, axis = 0)
[Amax, Bmax] = np.max(AB, axis = 0)
[Amidle, Bmidle] = np.median(AB, axis = 0) 
t = 0
for [A, B] in AB:
    t += abs(Amidle - A) + abs(A - B) + abs(Bmidle - B)

print(int(t))
# y = |x - A1| + |x - A2| + ... + |x - An|
#A1 <= A2 <= ... <= An
#上記の式でyが最小となるのはx = Amedianのとき            
            
        
    
    
    
    
        #間に合わない
     #enter in range(Amin, Amax + 1):
      #for mint = 10000000000000
      #for　exit in range(Bmin, Bmax + 1):
       # t = 0
        #for [A, B] in AB:
         # t += abs(A - enter) + abs(B - A) + abs(B - exit)
        #mint = min(mint, t)
    #print(mint)

      