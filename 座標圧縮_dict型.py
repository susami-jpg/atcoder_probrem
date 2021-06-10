# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:03:11 2021

@author: kazuk
"""

#辞書に初期値がない場合は、デフォルト値で初期化する
#defaultdictでできたのは辞書型ではなくタプルindex[0]がキーでindex[1]がvalue
from collections import defaultdict
data = defaultdict(int)
data['a'] += 1
data
#defaultdict(<class 'int'>, {'a': 1})
data['a'] += 1
#defaultdict(<class 'int'>, {'a': 2})


#defaultdict => dict 
d = defaultdict(lambda: defaultdict(int))
d['key']['a'] += 3

print(type(d))

d = dict(d)
print(type(d))


#Pythonの辞書（dict）のforループ処理（keys, values, items）
#keys(): 各要素のキーkeyに対してforループ処理 辞書オブジェクトをそのままfor文で回すとキーkeyが取得できる。
for k in d.keys():
    print(k)
#values(): 各要素の値valueに対してforループ処理
for v in d.values():
    print(v)
#items(): 各要素のキーkeyと値valueに対してforループ処理
for k, v in d.items():
    print(k, v)
    

#key昇順ソート
dct = { 2: 3, 3: 4, 1: 2, 0: 8, 4: 2 }
dct = sorted(dct.items())
print(dct)
#=> [(0, 8), (1, 2), (2, 3), (3, 4), (4, 2)]

dct = { 2: 3, 3: 4, 1: 2, 0: 8, 4: 2 }
for k, v in sorted(dct.items()):
    print(str(k) + ": " + str(v))
    
"""
0: 8
1: 2
2: 3
3: 4
4: 2
"""

#key降順ソート
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items(), key=lambda x: -x[0]):
    print(str(k) + ": " + str(v))

"""
4: 2
3: 4
2: 3
1: 2
0: 8
"""

#value昇順ソート
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items(), key=lambda x: x[1]):
    print(str(k) + ": " + str(v))

"""
1: 2
4: 2
2: 3
3: 4
0: 8
"""

#value降順ソート
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items(), key=lambda x: -x[1]):
    print(str(k) + ": " + str(v))

"""
0: 8
3: 4
2: 3
1: 2
4: 2
"""

#累積和をとる
d = dict(d)
prev = None
for key in d:
    if prev == None:
        prev = key
        continue
    d[key] += d[prev]
    prev = key
    
print(d)





