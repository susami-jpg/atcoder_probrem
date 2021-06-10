# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:45:39 2021

@author: kazuk
"""

#関数my_turnは探索を開始する節点nを受け取り、その評価値を返す関数である
#my_turnでは自分にとって最良の一手、すなわち最大の評価値を発見する
def my_turn1(n):
    #関数leafによって節点nが子を探索したりせずに直ちに評価できる節点かどうかの真偽値をかえす
    if leaf(n): 
        return evaluation(n) #直ちに評価できる場合は、関数evaluationによって評価値が与えられる
    max = 0 #下限値からはじめることで最大評価値の更新を可能にする
    for next in edge(n): #関数edgeはnの子のリストを返す
        temp = your_turn1(next) #tempはnの子についての評価値
        if temp > max: 
            max = temp #評価値の更新(nの子の評価値の中で最大の評価値を発見し、それをnの評価値とする(max))
    return max

#関数your_turnは探索を開始する節点nを受け取り、その評価値を返す関数である
#your_turnでは相手にとって最良の一手、すなわち(自分にとって)最小の評価値を発見する
def your_turn1(n):
    if leaf(n):
        return evaluation(n)
    min = 100
    for next in edge(n):
        temp = my_turn1(next) #tempはnの子についての評価値
        if temp < min: #相手は自分にとってもっとも評価値の低い一手を選ぶはず
            min = temp #最小評価値の更新
    return min

#各節点nは三目並べの盤面を意味するので、OとXと_の二重リストで与えられる(3*3)
#関数leafは盤面nを受け取り、nでゲームを終了しているかどうかを判定する。ゲームが終了するならばnの子は存在しないはずである。
def leaf(n):
    return ((triple(n, 'O') and not triple(n, 'X')) #Oの勝利
            or (not triple(n, 'O') and triple(n, 'X')) #Xの勝利
            or ('_' not in n[0] + n[1] + n[2])) #盤面が全て埋まっているとき
                                                #in n　とするとおそらくリストを探索してしまう

#関数tripleは盤面nと印pを受け取り、nの中でpが縦横斜めのいずれかでそろっているかどうかを判定
def triple(n, p):
    for (a, b, c) in [(0, 0, 0), (1, 1, 1), (2, 2, 2), (0, 1, 2)]:
        #(0, 0, 0)で一行目と一列目、(1, 1, 1)で二行目と二列目、(2, 2, 2)で三行目と三列目、(0, 1, 2)で斜めがそろっているかを判断
        if (n[a][0] == n[b][1] == n[c][2] == p or
            n[2][a] == n[1][b] == n[0][c] == p):
            return True
    return False

#関数evaluationは、そろったのがOならば100点、Xならば0点、引き分けならば50点を返す
def evaluation(n):
    if triple(n, 'O'):
        return 100 #O勝利時の評価点
    if triple(n, 'X'):
        return 0 #X勝利時の評価点
    return 50 #引き分け時

#関数edgeは盤面nに対してとりうる全ての手を全通り列挙し、次の盤面のリストを返す
def edge(n):
    L = n[0] + n[1] + n[2] #盤面を一連のリストに変換
    Ns = []
    player = 'O'
    if L.count('O') > L.count('X'): #countメソッドは引数に探したい文字列を受け取り、その数を返す
        player = 'X'
        #OとXどちらが多いかでどちらのターンかを判断
    for i in range(len(L)):
        if L[i] == '_': #空白のマスがあるときのみ実行
            L2 = L[:] #スライスで全指定、すなわちLのコピーをとっている。L自体を変更してしまうと次のループでその変更がくわえられた状態で始まってしまう
            L2[i] = player #空欄(_)にOかXをあてはめる
            Ns = Ns + [L2] #L2はある一つの想定盤面、それをforループで繰り返し、すべての想定盤面を網羅する
            #得られた想定盤面すべての場合をリストNsに追加する
    return [[[a, b, c], [d, e, f], [g, h, i]]
            for (a, b, c, d, e, f, g, h, i) in Ns] 
            #想定盤面全通りのリストNsに入っている想定盤面L2は一重リストなので二重リストにもどして返す(二重リスト(盤面)が複数存在するリストが返される)


#ミニマックス法を枝刈りで修正
#関数my_turnは、引数nの評価値がalpha以上beta以下でなければ、評価値を返す意味がないと判断して境界値(alphaまたはbeta)を返す
#すでに得られた評価値を基に、これから探索する節点の評価がどの範囲に入っていれば意味を持つかを計算して、alphaとbetaを更新している
def my_turn(n, alpha, beta):
    print(n, '= ? (' , alpha, '-', beta, ')')
    if leaf(n):
        return evaluation(n)
    for next in edge(n):
        temp = your_turn(next, alpha, beta) #子の評価値temp
        if temp > alpha: #現在分かっている下限値alphaより大きいtempを発見
            alpha = temp #下限値の更新
        if alpha >= beta: #上限値betaが分かっているときに、betaをalphaが超えることはないので、betaを返す
            return beta
    return alpha #betaを超えるようなtempが存在しなかったときはtempの最大値alphaを返す

def your_turn(n, alpha, beta):
    print(n, '= ? (' , alpha, '-', beta, ')')
    if leaf(n):
        return evaluation(n)
    for next in edge(n):
        temp = your_turn(next, alpha, beta)
        if temp < beta:
            beta = temp
        if beta <= alpha:
            return alpha
    return beta

n = [['O', '_', '_'], ['O', 'X', '_'], ['X', 'O', 'X']]
print(my_turn(n, 0, 100))