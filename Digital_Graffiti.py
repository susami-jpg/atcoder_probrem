# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:56:51 2021

@author: kazuk
"""

h, w = map(int, input().split())
hw = [list(input()) for _ in range(h)]

dxdy = [(0, 0), (0, 1), (1, 0), (1, 1)]
ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        #4マスのなかの黒の数を数えるパート
        cnt = 0
        for a, b in dxdy:
            y = i + a
            x = j + b
            if hw[y][x] == "#":
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
                
#右手法でといてみる  
#探索する方向を現在地を基準に、下、右、上、左で定義している
dir = [[1,0], [0,1], [-1, 0], [0, -1]]

#初期値の設定を、現在地の座標( x, y )、回転数(cnt)、方向 ( d ) としている。
#d がゼロなので、最初は下向き。
#スタート地点は以下で定義しているが、その定義から頂点であることは自明なのでcnt=1を初期値とする
cnt, d = 1, 0

#mapを二倍にして右手法をやりやすくする
thw = []
for row in hw:
    new = []
    for i in row:
        new += 2 * i
    thw.append(new)
    thw.append(new)

for i in range(2, 2 * h):
    for j in range(2, 2 * w):
        if thw[i][j] == "#":
            x = i
            y = j
            break
    else:
        continue
    break

seen = [[0] * 2 * w for _ in range(2 * h)]
    
#探索した迷路上の座標点のもつ値が 1 だったら終了(=ゴール)、それまでは探索続ける。
#また、探索完了した座標点のもつ値は 2 に更新される。
while 1:
    if seen[x][y]:
        break
    seen[x][y] = 1
    #次に進むべき方向性を探るための試行回数分だけ繰り返しを行っていく、
    for i in range(len(dir)):
        j = (d + i -1) % len(dir) # 下を向いていたら、「右側」は左ですよね。(0+0-1)%4=3です。jは3,0,1,2と変化します。下を向いている時の「右側」とは、迷路全体のどっち方向ですか？
        #探索していない地点で進行可能な場合
        if thw[x + dir[j][0]][y + dir[j][1]] == "#":
            x += dir[j][0]
            y += dir[j][1]
            if d != j:
                cnt += 1
            d = j
            break

print(cnt)


#右手法アルゴリズム　参考
#右手法の基本ルール (右行けるなら右、右行けないなら直進、直進できないなら、左) 
maze = [
    [9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 9],
    [9, 0, 9, 0, 1, 9],
    [9, 0, 9, 0, 0, 9],
    [9, 9, 9, 9, 9, 9],
]


#探索する方向を現在地を基準に、下、右、上、左で定義している
dir = [[1,0], [0,1], [-1, 0], [0, -1]]

#初期値の設定を、現在地の座標( x, y )、移動量 (depth)、方向 ( d ) としている。
#d がゼロなので、最初は下向き。
x, y, depth, d = 1, 1, 0, 0

#探索した迷路上の座標点のもつ値が 1 だったら終了(=ゴール)、それまでは探索続ける。
#また、探索完了した座標点のもつ値は 2 に更新される。
while maze[x][y] != 1:
    maze[x][y] = 2
    #次に進むべき方向性を探るための試行回数分だけ繰り返しを行っていく、
    for i in range(len(dir)):
        j = (d + i -1) % len(dir) # 下を向いていたら、「右側」は左ですよね。(0+0-1)%4=3です。jは3,0,1,2と変化します。下を向いている時の「右側」とは、迷路全体のどっち方向ですか？
        #探索していない地点で進行可能な場合
        if maze[x + dir[j][0]][y + dir[j][1]] < 2:
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        #この行以降(下記のパート)、探索済みで進行可能な場所であればそこへ進み、各種の変数を更新するという理解です。
        elif maze[x + dir[j][0]][y + dir[j][1]] == 2:
                  x += dir[j][0]
                  y += dir[j][1]
                  d = j
                  depth -= 1
                  break

print(depth)