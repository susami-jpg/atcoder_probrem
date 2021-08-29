# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:29:11 2021

@author: kazuk
"""


#複数の数字のリストを渡すとそれらの公約数を列挙したリストを返す
def check(num, i):
    for n in num:
        if n % i != 0:
            return False
    else:
        return True

def make_divisors(num):
    lower_divisors , upper_divisors = [], []
    i = 1
    min_n = min(num)
    while i*i <= min_n:
        if check(num, i):
            lower_divisors.append(i)
        if i != min_n // i and check(num, min_n // i):
            upper_divisors.append(min_n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
num = list(map(int, input().split()))
for ans in make_divisors(num):
    print(ans)
    
