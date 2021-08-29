# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:39:19 2021

@author: kazuk
"""

"""
長さの配列を用意しての倍数に、1の倍数に+1、2の倍数に+1、3の倍数に+1、……と
割り切れる数に足していくだけです
"""
def num_divisors_table(n):
    table = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1
    
    return table

print(num_divisors_table(9))


"""
高度合成数
1以上の整数を考えた時、自分より小さい数よりも約数の数が大きい物を高度合成数と呼ぶらしいです
"""
import collections

def prime_factor_table(n):
    table = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if table[i] == 0:
            for j in range(i + i, n + 1, i):
                table[j] = i
    
    return table

def prime_factor(n, prime_factor_table):
    prime_count = collections.defaultdict(int)
    
    while prime_factor_table[n] != 0:
        prime_count[prime_factor_table[n]] += 1
        n /= prime_factor_table[n]
    
    if n > 1:
        prime_count[n] += 1
    
    return prime_count

def num_divisors(prime_count):
    num = 1
    
    for prime, count in prime_count.iteritems():
        num *= (count + 1)
    
    return num

