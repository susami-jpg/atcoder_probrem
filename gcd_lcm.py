# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:59:42 2021

@author: kazuk
"""


import functools

"""
def euclid(a, b):
    while b:
        a, b = b, a%b
    return a
"""

#2整数の最大公約数を求める
#再帰関数を使う場合
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

#N個の整数の最大公約数を求める(numsはN個の整数のリスト)
def gcd(nums):
    return functools.reduce(euclid, nums)

#2整数の最小公倍数を求める
def multiple(a, b):
    return a*b // euclid(a, b)

#N個の整数の最小公倍数を求める(numsはN個の整数のリスト)
def lcm(nums):
        return functools.reduce(multiple, nums)

