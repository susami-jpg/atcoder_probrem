# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:52:16 2021

@author: kazuk
"""

import pandas as pd
import matplotlib.pyplot as plt
#matplotlib.pyplotの記述を簡略化。書式は　import モジュール名 as 名前  以降はここでつけた名前でモジュールを利用できる。
#asは～としてという意味でつかわれるため、元のモジュール名を簡略化後の名前とするという意味になる。

df = pd.read_csv('mydata.csv')
#データフレームの作成。書式　pandas.read_csv(CSVファイル名)　このファイルと別の場所にあるcsvファイルを指定する場合は、パス名をつける。

print(df.describe())
#平均などの基本的な統計による８種類の分析　describe関数　データフレーム.describe() print関数をに代入することでコンソールで確認できる。

print(df.corr())
#相関分析を行うコード　corr関数　データフレーム.corr()
#pandasモジュールで使えるデータ分析の関数　var分散　median中央値　value_counts値の頻度　pivot_tableクロス集計

plt.scatter(df['気温'], df['物質A'])
#散布図の作成にはmatplotlib.pyplotモジュールのscatter関数を使う。書式は　matplotlib.pyplot.scatter(列１,列２)
#データフレームから指定した列を取り出す書式。書式　データフレーム[列名]　列名は文字列なら'で囲う。

plt.show()
#散布図を描画するには、matplotlib.pyplot.show関数を使う。書式は上記の通りで引数はない。


