# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 02:19:46 2021

@author: kazuk
"""

#PyPyでscipyはRE
#python3なら通る
from scipy.special import comb
l = int(input())

#exact=Trueでintで答えを取得
print(comb(l-1, 11, exact=True))
