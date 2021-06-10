# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:57:35 2021

@author: kazuk
"""

import math
math.pow(2, 3)
#mathモジュールのpow関数。xのy乗。

import random
random.randint(0, 100)
#randint関数。引数を二つ渡すとその間で乱数を生成して返す。

import statistics
nums = [0, 3, 45, 594, 43, 45]
statistics.mean(nums) #平均
statistics.median(nums) #中央値
statistics.mode(nums) #最頻値

#ある文字列がPythonのキーワードかどうかをチェック
import keyword
keyword.iskeyword('for')
keyword.iskeyword('football')

#import csv

#with open('st.csv', 'w', newline='') as f:
    #st.csvがなければ新しくファイルを作成する。
    #w = csv.writer(f, delimiter = ',')
    #w.writerow(['one', 'two', 'three'])
    #w.writerow(['four', 'five', 'six'])
    #writerow関数は一度の呼び出しで一行しか書けない。二行書くなら二回呼び出す。
    

with open('tstp/project.py', 'r', encoding='utf-8') as f:
    print(f.read())
    
w = input('質問は何ですか?:')
with open('tstp/project.py', 'w', encoding='utf-8') as t:
    t.write(w)

import csv
lin = [['トップガン', 'Riskey Business', 'Minority Report'], ['Titanic', 'The Revenant', 'Invception'], ['Man on Fire', 'Flight']]
with open('st.csv', 'w', newline='', encoding='cp932') as l:
    w = csv.writer(l, delimiter = ',')
    for i in lin:
        w.writerow(i)
        
        