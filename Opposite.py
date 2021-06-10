# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:12:17 2021

@author: kazuk
"""

import math, cmath
n = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())
xo = (x0 + xh) / 2
yo = (y0 + yh) / 2
#complex型は複素数を表す　実部、虚部の順
vector = complex(x0 - xo, y0 - yo)
#長さが1で偏角が2πNの複素数をrとすると、答えはp=(p0−o)r+oです。
#cmath.polar(x) xの極座標表現を返します。
#cmath.rect(r, phi) 極座標 r, phi を持つ複素数 x を返します。
r = cmath.rect(1, 2*math.pi/n)
ans = complex(xo, yo) + vector * r
print(ans.real, ans.imag)

