# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:14:30 2021

@author: kazuk
"""


age = 25
if age <= 10:
    print('幼少期')
elif age > 10 and age <= 30:
        print('青年期')  
#if文はTrueならば実行する。
else :
    print('老年期')

#累乗：**  剰余:%  商://
#論理演算子　and 左右がTrueなら戻り値True, or どちらかがTrueなら戻り値True, not 'not -'が正しければTrue。


#入れ子のif 二つの条件両方が満たされて時のみ実行される。
x = 10
y = 11
if x == 10:
    if y ==11:
        print(x + y)

#数学関数f(x)=x*2をPythonで定義する。
def f(x):
    return x*2

age = input('Enter your age:')
#input関数　文字列を引数として受け取り、コンソールに表示。プログラムを実行する人が返答を入力できる。
int_age = int(age)
#int関数　整数の文字列や浮動小数点を受け取り、整数オブジェクトを返す。float関数は浮動小数点数オブジェクトを返す。

if int_age < 21:
    print('You are young')
else:
    print('Wow, You are old!')
    
x = int(input('数字を入力:'))
def h(x):
    """

    Parameters
    ----------
    x : int.

    Returns:int x*2
    -------
   
    """
    return x**2
print(h(x))

def five(a,b,c,d=2,e=5):
    return a + b*2 + c*3 + d*4 + e*5
print(five(2, 4, 6))

t = int(input('数字を入力:'))
def ev(t):
    return t//2
print(ev(t))

h = int(ev(t))
def fv(h):
    return h*4
print(fv(h))

try:
    s = input('整数オブジェクトか数字の文字列を入力:')
    print(float(s))
except(ValueError):
    print('Invalid input')
    


    