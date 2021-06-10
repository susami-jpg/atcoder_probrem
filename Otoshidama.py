# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:16:38 2021

@author: kazuk
"""
N, Y = map(int, input().split())
for i in range(N + 1): #外のループ(10000)
  for j in range(N + 1 -i): #内のループ(5000)
    if i + j > N:
      continue
    k = N - i - j
    if 10000 * i + 5000 * j + 1000 * k == Y:
      print(i, j, k)
      break #答えが見つかった時点で内側のループを終了
  else: #答えが見つからなかったときは外側のループは終わらない
      continue
  break
else: #二重ループが正常に終了、すなわち答えが見つからなかったとき
  print(-1, -1, -1)
      