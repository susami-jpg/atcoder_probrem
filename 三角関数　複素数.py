# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 17:41:44 2021

@author: kazuk
"""

import math

#円周率
pi = math.pi

#ラジアン -> 度
math.degrees(pi)

#度　-> ラジアン
math.radians(pi)

#sin
sin30 = math.sin(math.radinans(30))

#度数法で角度を与えるとそのsinを返す
def sin_x(degree):
    import math
    rad = math.radians(degree)
    return math.sin(rad)

def cos_x(degree):
    import math
    rad = math.radians(degree)
    return math.cos(rad)

def tan_x(degree):
    import math
    rad = math.radians(degree)
    return math.tan(rad)

#sin -> 度
def asin_x(x):
    import math
    x = math.asin(x)
    return math.degrees(x)

def acos_x(x):
    import math
    x = math.acos(x)
    return math.degrees(x)

def atan_x(x):
    import math
    x = math.atan(x)
    return math.degrees(x)

"""
atan2 関数とは
(x, y)を引数にとり (ただし (y, x)の順にとるので注意)、ベクトル (x, y)の指す”向き”を返します
向きは右向き 
(x 軸の正の向き ) を 0 とし、反時計回りを正とするラジアンで返されます
例えば 
atan2(0, 3) = 0 (x=3, y=0で右向きだから)
atan2(2, 0) = π/2 (x=0, y=2は上方向)
"""
print(math.degrees(math.atan2(-0.0, -1)))
# -180.0

#atan2_xはベクトル(x, y)をもらい、その方向を度数法で返す
def atan2_x(x, y):
    import math
    x = math.atan2(y, x)
    return math.degrees(x)

#print(math.degrees(math.atan2(1, 1)))
# 45.0

#print(math.degrees(math.atan2(1, 0)))
# 90.0

#print(math.degrees(math.atan2(1, -1)))
# 135.0

#print(math.degrees(math.atan2(0, -1)))
# 180.0

#print(math.degrees(math.atan2(-1, -1)))
# -135.0

#print(math.degrees(math.atan2(-1, 0)))
# -90.0

#print(math.degrees(math.atan2(-1, 1)))
# -45.0


#complex型は複素数を表す　実部、虚部の順
vector = complex(2, 3)

#長さが1で偏角が2πNの複素数をrとすると、答えはp=(p0−o)r+oです。
#cmath.polar(x) xの極座標表現を返します。
#cmath.rect(r, phi) 極座標 r, phi を持つ複素数 x を返します。
import cmath
n = 6
r = cmath.rect(1, 2*math.pi/n)
ans = complex(1, 3) + vector * r

#rotateは複素数compと偏角(ラジアン)radを受け取ってcompを偏角だけ回転した複素数を返す
def rotate(comp, rad):
    import cmath
    return comp*cmath.rect(1, rad)
    