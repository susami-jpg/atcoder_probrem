
#n進数
########関数部分##############
def Base_10_to_n(X, n):
    if X == 0:
        return "0"
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = X_dumy//n
    return out
############################
"""
Xもnもint
戻り値はstr

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
Xはstr
nはint
戻り値はint

print(Base_n_to_10('253',4))#"55"と表示される．
"""

def Base_a_to_b(n, a, b):
    n = str(n)
    a = int(a)
    b = int(b)
    n10 = Base_n_to_10(n, a)
    nb = Base_10_to_n(n10, b)
    return nb

from sys import exit
N, K = map(int, input().split())
for _ in range(K):
    n9 = str(Base_a_to_b(N, 8, 9))
    if n9 == "0":
        print(0)
        exit()
    N = n9.replace('8', '5')
    
while len(N) >= 2:
    if N[0] == "0":
        N = N[1:]
    else:
        break
print(N)

