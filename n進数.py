# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:13:06 2021

@author: kazuk
"""


########関数部分##############
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
############################
"""
#####関数をつかってみる．#####
######今回は二進数に変換######
x10 = 35
x2 = Base_10_to_n(x10, 2)
print( x2 )#"100011"が表示される．
"""

########関数部分##############
def Base_10_to_n_rec(X, n):
    if (int(X/n)):
        return Base_10_to_n_rec(int(X/n), n)+str(X%n)
    return str(X%n)
############################
 
"""
#####関数をつかってみる．#####
######今回は二進数に変換######
x10 = 35
x2 = Base_10_to_n(x10, 2)
print( x2 )#"100011"が表示される．
"""

########関数部分##############
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out
############################
"""
print(Base_n_to_10('253',4))#"55"と表示される．
"""

def change(N,shinsu):
    keta=0
    for i in range(10**9):
        if N<shinsu**i:
             keta+=i
             break
    ans=[0]*keta
    check=0
    for i in range(1,keta+1):
        j=N//(shinsu**(keta-i))
        ans[check]=j
        check+=1
        N-=(j)*(shinsu**(keta-i))
    return ans