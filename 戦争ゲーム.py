# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:49:34 2021

@author: kazuk
"""

class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    
    values = [None, None,
              '2', '3', '4', '5', '6', '7', '8', '9', 
              '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, v, s):
        """スート(マーク)も値も整数値です。"""
        self.value = v
        self.suit = s
        
    def __lt__(self, c2):
        #__lt__(self, other)はselfがotherより小さいかどうかを調べる特殊メソッド。
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        #__gt__(self, other)はselfがotherより大きいかどうかを調べる特殊メソッド。
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        #__repr__オブジェクトを表す公式な文字列を生成する特殊メソッド。そのままではいまいち何を指すのかわからない、
        #print関数にオブジェクトをそのまま入力するとオブジェクトの位置が返ってくる。
        v = self.values[self.value] + ' ' + 'of' + ' ' + self.suits[self.suit]
        return v

from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
        #deck = Deck()
        #for card in deck.cards:
            #print(card)
            #上記のコードで52枚のカードを出力できる。Deckクラスの変数はselfしか指定されていないため、Deck()、すなわち引数を入力しなくてよい。
            #変数deckには.cardsによって52枚のカードが作成され、シャッフルされた後、一枚ずつ変数cardに引き渡されてprint関数で出力される。
            
            
    def draw(self):
        if len(self.cards) == 0:
            return #cardsリストが0になったらNoneを返す。
        return self.cards.pop() #cadsリストから要素を一つ削除してその要素を返す。popメソッドは引数を指定しなければリストの末尾を選ぶ。
    
 
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input('プレイヤー1の名前:')
        name2 = input('プレイヤー2の名前:')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def print_winner(self, winner):
        w = 'このラウンドは{}が勝ちました。'
        print(w.format(winner.name))
        
    def print_draw(self, p1, p2):
        d = '{}は{}、{}は{}を引きました。'
        print(d.format(p1.name, p1.card, p2.name, p2.card))
        
        
    def play_game(self):
        cards = self.deck.cards
        print('戦争を始めます。')
        while len(cards) >= 2:
            m = 'qで終了、それ以外のキーでPlay:'
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card: #draw関数によってスート(suits)と数字(value)のカード情報に変換されたオブジェクトが、__lt__ or __gt__の特殊関数によってどちらが大きいか評価される。
                self.p1.wins += 1 #勝利回数の追加(もとは0.)
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)
                
        win = self.winner(self.p1, self.p2)
        print('ゲーム終了、{}の勝利です!'.format(win))
        
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return '引き分け!'
    
    
game = Game()
game.play_game()       
