# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:42:35 2021

@author: kazuk
"""
#メモリ超過で通らない
N = int(input())
p = []
for _ in range(N):
    x, y = input().split()
    p.append((int(x), int(y)))
setp = set(p)
    
maxval = 0

#N個の点から二点を選び出し、ベクトルを生成
for i in range(N - 1):
    for j in range(i + 1, N):
        vectorxy = (p[i][0] - p[j][0], p[i][1]-p[j][1]) #setpについてこの操作は行えない(setはindexを指定できない)
        #選び出した二点によって決まる正方形(2通り考えられるが、1通りだけ考えればよい)を形成する残りの二点を見つける
        #vector1 = (p[i][0], p[i][1])
        #vector2 = (p[j][0], p[j][1])
        #vectorxyはvector1と2をつなぐベクトル
        #vectorxyに垂直なvectorは(vectorxy[1], -vectorxy[0])か(-vectorxy[1], vectorxy[0])
        #考える正方形は一通りでよいので上記のどちらかを垂直ベクトルとしてつかう
        vector3 = (p[i][0] + vectorxy[1], p[i][1] - vectorxy[0])
        vector4 = (p[j][0] + vectorxy[1], p[j][1] - vectorxy[0])
        if vector3 in setp and vector4 in setp: #inをlistに対して行うとめっちゃ遅い
            maxval = max(maxval, vectorxy[0] ** 2 + vectorxy[1] ** 2)
            
print(maxval)
        
