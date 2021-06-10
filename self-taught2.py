# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 01:14:12 2021

@author: kazuk
"""
intro = {'身長': '174cm', '好きな色': '黒', '好きな作家': '森博嗣'}

try:
    x = str(input('キーワードを入力:'))
    if x in intro:
        print(intro[x])
    else:
        print('その項目はありません。')
except(ValueError):
    print('Invalid input')
    #except文はエラー名を指定しなくてもよい(エラーならばどんなものでもそれ以降に指定した処理を実行する。)
    
intro['サザンオールスターズ'] = ['シャッポ', 'マチルダ', 'ダーリン']
print(intro['サザンオールスターズ']) 

#formatメソッド
what = input('何が:')
when = input('いつ:')
where = input('どこで:')
do = input('どうした:')

r = '{}は{}に{}で{}。'.format(what, when, where, do)
print(r)

content = input('内容:')
who = input('誰:')
m = '私は昨日{}を書いて、{}に送った!'.format(content, who)
print(m)

tv = ['got', 'narcos', 'vice']
for i, new in enumerate(tv):
    #enumerate() インデックス番号、要素の順に取り出すことのできる関数。上記の例だとiがインデックス関数でnewが要素を表す変数。
    new = tv[i]
    new = new.upper()
    tv[i] = new
    
print(tv)

#enumerate関数の例
#for i, new in enumerate(tv):
    #print(i, new)
#0 got
#1 narcos
#2 vice

#while文　条件が満たされる限り実行し続ける。
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print('Happy New Year!')

#break文　ループを終了するための文。
for i in range(110):
    print(i)
    break

#continue文　実行途中の反復処理を途中で終了して、次の反復処理を開始する。break文と異なり、continue文ではループは終了せず、continueの後にあるコードを実行せずに次のループに入る。
for i in range(5):
    if i == 3:
        continue
    print(i)
    
mov = ['ウォーキング・デッド', 'アントラージュ', 'ザ・サプライズ', 'ヴァンパイア・ダイアリーズ']
for i in mov:
    print(i)
    
for i in range(25,51): #range(,)　始値はその数字のままだが、終値は引数-1。
    print(i)

ans = [1, 4, 9, 16]

#数当てゲーム
while True:
    try:
        n = input('数字を入力してください:')
        
        if n == 'q':
            break
        else:
            if int(n) in ans:
                print('正解')
            else:
                print('不正解')
            
    except(ValueError):
        print('数字を入力するか、qで終了します。')

#2つのリストに含まれる数字のかけ合わせの組み合わせ
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
com = []

for i in list1:
    for t in list2:
        m = i * t
        com.append(m)
print(com)







