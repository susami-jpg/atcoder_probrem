# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:04:09 2021

@author: kazuk
"""

import sys
def check(bini):
    stack = []
    for i in bini:
        if not stack:
            stack.append(i)
        elif i == '0':
            stack.append(i)
        else:
            if stack[-1] == '0':
                stack.pop()
    if stack:
        return False
    else:
        return True
    
n = int(input())
if n % 2 == 1:
    sys.exit()
        
else:
    for i in range(1 << n):
        bini = list(bin(i)[2:])
        bini = ['0'] * (n - len(bini)) + bini
        if check(bini):
            bini = ''.join(bini)
            bini = bini.replace('0', '(').replace('1', ')')
            print(bini)
        
    
    