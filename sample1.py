# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:20:42 2021

@author: kazuk
"""

import os
import shutil
import datetime

MY_DIR='photo/'
fldnum=0

files=os.listdir(MY_DIR)
#os.listdirでフォルダ内にあるファイルをリスト化する
#リスト　x=[2,4,6,7]など

for i in files:
    mtime = os.path.getmtime(MY_DIR + i)
    dt = datetime.datetime.fromtimestamp(mtime)
    dpath = MY_DIR + dt.strftime('%Y%m%d')
    #日付データ.strftime(形式)　で日付データを文字列に変換　これはモジュールではなくオブジェクトとメソッドを使っている。
    #　%Y 4桁の西暦年　%y下二けたの西暦年　%m　二桁の月　%d　二桁の日　形式は文字列ならば''をつけるのを忘れずに。
    
    if os.path.isdir(dpath)==False:
        #os.path.isdirでフォルダを探す　isfileでファイルをさがす
        os.mkdir(dpath)
        fldnum+=1
        #　+=で変数に1を加える
    
    shutil.move(MY_DIR + i, dpath)
    #shutil.move(ファイル名,移動先フォルダ名)
    
print(str(fldnum) + '個のファイルを作成しました。')
#str()で数値を文字列に変換

#os.makedirs(フォルダー名, exists_ok = True ) で既存のフォルダ名と同じフォルダがある場合新規フォルダを作成しない関数
#os.path.join(パス1,パス2,...)でフォルダ名とファイル名の連結　演算子+を使わなくてよいしパス(/)は勝手に入れてくれる。
#len(os.listdir(MY_DIR)フォルダー数は組み込み関数の「len」関数で数えます。len関数は引数にリストを指定すると、そのリストの要素数を数値として取得できます。
#if構文について
#if 条件式:
    #条件成立時に実行する処理
#(elif 条件式：
    #条件成立時に実行する処理
#...)
#else:
    #条件不成立時に実行する処理(elseの記述がなければ不成立時に何も実行しないという設定)
  
#for構文について
#for 変数 in range(繰り返す回数):
    #繰り返す処理
#for 変数 in リスト名:
    #繰り返す処理
    #(変数には0,1,2,..)と代入されていく
    #上記の構文の場合リスト名[0],リスト名[1]...と指定されていく


#while構文　指定した条件が成立している間繰り返し処理する
#while (条件式):
    #繰り返す処理
    
