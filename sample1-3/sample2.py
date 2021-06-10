# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:48:38 2021

@author: kazuk
"""

import requests
import bs4
import csv

try:

    rs = requests.get('http://tatehide.com/bbdata.php')
    #request.get(目的のWebページのURL)でwebページのhtmlを取得。URLは文字列。
    sp = bs4.BeautifulSoup(rs.text.encode(rs.encoding), 'html.parser')
    #request.get関数で得たhtml情報を切り出せる形に変換。
    
    rcd = []
    rcd.append(sp.select_one('#date').string)
    #sp.select_one('#date').stringでidの内容を取得。
    
    for elm in sp.select('.val'):
        rcd.append(elm.string)
        #for 変数　in リスト名(class)で、３つの要素からなるリストを変数rcdで定めた新しいリストに代入。
    
    with open('mydata.csv', 'a', newline='') as f:
    #open関数で目的のcsvファイルを開く。書式はopen(目的のcsvファイル名, 'a', newline = '')
    #目的のcsvファイルは拡張子までつける。'a'はデータを追記する形式。newline=''はこういうもの。
    #open関数の戻り値は開いたファイルのファイルオブジェクトである。よって変数名で指定しておくと以降ファイルオブジェクトを指定するのに便利。
    
        wrtr = csv.writer(f, delimiter=',')
        #データ書き込み用のオブジェクトの作製　csvモジュールのwriter関数　csv.writer(ファイルオブジェクト,delimiter=',') 第二引数はデータの区切りがカンマであることを指定。
        #Writer関数は戻り値としてデータ書き込み用オブジェクトWriterオブジェクトを返す。これは通常変数に代入して使う。
        
        wrtr.writerow(rcd)
        #データを追加して保存　writerowメソッド　Writerオブジェクト.writerow(リスト)
        
   # f.close()
    #closeメソッドでファイルを閉じる。ファイルオブジェクト.close()
    
except requests.exceptions.RequestException as e:
    print('通信でエラー発生:{}'.format(e.args))
    #as eと:{}'.format(e.args)を付け加えることでエラーの詳細をコンソールに表示。
    
except OSError as e:
    print('ファイル処理でエラー発生:{}'.format(e.args))
    
#sp.select('.val')はclassについてのリスト(今回の場合は、気温、物質、交通量の三つからなるクラスをリストとして変数に代入した。)

#bs4.BeautifulSoup(HTMLデータ, パーサーの種類)でhtmlの要素を切り出せる形に変換。切り出して得られた戻り値をBeautifulSoupオブジェクトと呼ぶ。
#Responseオブジェクト.text.encode(Responseオブジェクト.encoding)　Responseオブジェクトはrequest.get関数の戻り値
#パーサーはhtmlを解析して切り出すプログラム　html.parserを指定すればよい
#get関数で得られた戻り値を代入した変数をrsとするなら、Responseオブジェクトは「rs.text.encode(rs.encoding)」となる。このように決まっていると単純に考えてよい。

#beautifulsoupオブジェクトから要素を切り出す方法は二つある。select_oneメソッドとselectメソッドである。

#select_oneメソッド　指定した一つの要素を取得。
#Beautifulsoupオブジェクト.select_one(CSSセレクタ)
#CSSセレクタは文字列で指定。要素を特定するための仕組みのこと。#id名で指定したid名の一つを取得。

#selectメソッド　指定した複数の要素を取得。
#Beautifulsoupオブジェクト.select(CSSセレクタ)
#CSSセレクタは文字列で指定。要素を特定するための仕組みのこと。タグ名か.class名を入れる（class名の前には.をいれる。))
#.select(CSSセレクタ)[0]のようにCSSセレクタの後に[インデックス番号]を入れると個々の要素を取り出せる。


#要素内容のみを取り出す場合は、要素.string（開始タグと終了タグで囲まれた部分が要素内容）

#空のリストを用意し、要素を入れていく。　変数名=[]　→　リスト名(変数名).append(追加する要素)

#appendメソッドの代わりに使えるリスト内包表記
#書式　[変数　for 変数　in 集合]
#ex) [elm for elm in sp.select('.val')]でsp.select('.val')によって取得されたhtml要素が、変数elmに順次代入され、それらを要素とするリストが作成される。
#ほかにもリスト内包表記は、変数に何かしらの処理を施してリストを作成できる。
#書式　[変数を使った処理 for 変数　in　集合]
#ex) [elm.string for elm in sp.select('.val')]

#例外処理　try文とexcept文
#try:
#   通常時の処理
#except 検知したいエラーの種類 as エラーの変数:
#   エラー時の処理

#通信関係の例外処理　エラーの種類にrequests.exceptions.RequestsExceptionを指定
#requestsモジュールのエラーでは、特例的にデータ取得を失敗した際のエラーは、プログラマが主導で発生させる必要がある。
#データ取得失敗のエラーを手動で発生させるコード　Responseオブジェクト.raise_for_status()

#csvファイル関係の例外処理
#with open関数でファイルを開く処理 as 変数:
    #ファイルの処理
#asに続けて指定する変数で開いたファイルのファイルオブジェクトが変数に代入される、
#with文を使うとエラーの有無に関わらずファイルを閉じる。ただし、python以外のアプリで開いたファイルに関してはその限りではない。
#上記よ李close関数が省略できる。
