# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:21:34 2021

@author: kazuk
"""

import random
list1 = ['cat', 'fox', 'dog', 'cap', 'tex', 'ant']
word = random.choice(list1)

def hangman(word):
    wrong = 0
    stages = ['',
              '_______       ',
              '|             ',
              '|      |      ',
              '|     　0      ',
              '|     /|\     ',
              '|     / \      '
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = '一文字を予想してください。:'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '＄'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け!正解は　{}'.format(word))
        
hangman(word)

            
        