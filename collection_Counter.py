# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 01:38:50 2021

@author: kazuk
"""

from sys import exit
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

print(type(c))
# <class 'collections.Counter'>

print(issubclass(type(c), dict))
# True

from collections import Counter
n = input()
if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
cnt = Counter(n)
for i in range(112, 1000, 8):
    #同じ動作はマイナス(‘-‘)演算子を使っても出来ます
    #マイナスの場合存在しない要素を除算するとそのキーはなくなる
    if not Counter(str(i)) - cnt:
        print("Yes")
        exit()
print("No")

"""
要素から他のイテラブルの要素をひく
subtract([iterable-or-mapping])を使います。
カウントは置き換えではなく、引かれます。

# 元のCounterオブジェクト
>>> c1 = collections.Counter('abbcabbbccca')
>>> c1
Counter({'b': 5, 'c': 4, 'a': 3})

# 要素のカウンターを引きます
>>> c1.subtract({'b':1, 'c':1, 'a':1})
>>> c1
Counter({'b': 4, 'c': 3, 'a': 2})

# カウンター値は0やマイナスも可能。存在しない要素を除算するとマイナスになる
>>> c1.subtract({'e':1, 'c':3, 'a':3})
>>> c1
Counter({'b': 4, 'c': 0, 'a': -1, 'e': -1})
Copy
同じ動作はマイナス(‘-‘)演算子を使っても出来ます
マイナスの場合存在しない要素を除算するとそのキーはなくなる
"""