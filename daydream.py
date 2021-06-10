# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:10:26 2021

@author: kazuk
"""

s = input()

while s:
    if s[:6] == "eraser":
        s = s[6:]
    elif s[:5] == "erase":
        s = s[5:]
    elif s[:5] == "dream":
        if s[5:8] == "era":
            s = s[5:]
        elif s[5:7] == "er":
            s = s[7:]
        else:
            s = s[5:]
    else:
        print("NO")
        break
else:
    print("YES")

s = input()
if s.replace("eraser"," ").replace("erase"," ").replace("dreamer"," ").replace("dream"," ").replace(" ", ""):
    print("NO")
else:
    print("YES")
    
import re
s = input()
print("YES" if re.match("^(eraser?|dream(er)?)*$", s) else "NO")
#正規表現の^と$は文字列の先端と末尾を示しています。A|BはA, Bのうちのどれかを示します。?は直前の正規表現があってもなくてもいいとする表記です(eraser?はeraseもしくはeraser)。*は直前の正規表現を繰り返したものにマッチさせる表現です。


    