# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:26:59 2021

@author: kazuk
"""

n, k = map(int, input().split())
from sys import exit

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
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out
############################
"""
print(Base_n_to_10('253',4))#"55"と表示される．
"""

def eight_to_nine(n):
    n10 = Base_n_to_10(str(n), 8)
    return Base_10_to_n(int(n10), 9)

def nine_to_eight(n):
    n10 = Base_n_to_10(str(n), 9)
    return Base_10_to_n(int(n10), 8)

ans = eight_to_nine(n)
for _ in range(k):
    ans = ans.replace("8", "5")
    ans = eight_to_nine(ans)
ans = nine_to_eight(ans)

while len(ans) >= 2:
    if ans[0] == "0":
        ans = ans[1:]
    else:
        break

print(ans)

        
    
