# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:41:08 2021

@author: kazuk
"""

from math import sin, radians
A, B, C = map(int, input().split())
def f(t):
    return A*t + B*sin(radians(C*t*180))-100

from scipy import optimize

print(optimize.bisect(f, 0, 200))


from math import sin, radians
A, B, C = map(int, input().split())
def f(t):
    return A*t + B*sin(radians(C*t*180))-100

def bisect(f,a,b):
    #少数第何位までの誤差をゆるすか
    eps = 0.000001
    #print("n\tc\tf(c)")
    n = 1
    while True:
        c = (a + b)/2
        #print("{}\t{:.5f}\t{:.5f}".format(n, c, f(c)))
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        n += 1
        if abs(f(c)) < eps: # or abs(a - b) < eps
            break
    
    return c

print(bisect(f, 0, 200))