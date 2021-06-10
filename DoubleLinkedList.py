# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 01:55:18 2021

@author: kazuk
"""

class Node(object):
    def __init__(self, num, prv = None, nxt = None):
        self.num = num
        self.prv = prv
        self.nxt = nxt
 
 
class DoublyLinkedList(object):
    def __init__(self):
        self.start = self.last = None
 
    def insert(self, num):
        new_elem = Node(num)
 
        if self.start is None:
            self.start = self.last = new_elem
        else:
            new_elem.nxt = self.start
            self.start.prv = new_elem
            self.start = new_elem
 
    def delete_num(self, target):
        it = self.start
        while it is not None:
            #itがself.lastまでいって次のNoneになれば全てを探索したことになるのでループ終了。
            if it.num == target:
                #itの数字が削除すべき数字targetと一致した時
                if it.prv is None and it.nxt is None:
                    self.start = self.last = None
                    #Nodeがstartのみの時、すなわち前後はNoneの時、startをNoneに
                else:
                    if it.prv is not None:
                        it.prv.nxt = it.nxt
                        #itの前がある場合は、it.prvの次、すなわちit.prv.nxtをit.nxtとすることでitを削除する。
                    else:
                        self.start = self.start.nxt
                        #itが先頭である場合、startをstart.nextとして(it.nxtと同じ)、itを削除する。
 
                    if it.nxt is not None:
                        it.nxt.prv = it.prv
                        #itの後がある場合はit.nxtの前のNode、すなわちit.nxt.prvをit.prvとすることでitを削除する。
                    else:
                        self.last = self.last.prv
                        #itの後ろがないすなわちitがlastならば、lastをlast.prvとすることでitを削除する。              
                        break
                    #if節内に入った場合はtargetが見つかり、削除されたということなのでループ終了。
            it = it.nxt
            #startから始まり、一回ループするごとにnxtに行くことでtargetを探す。
            
    def delete_start(self):
        if self.start is self.last:
            self.start = self.last = None
        else:
            self.start.nxt.prv = None
            #これをやらないとself.start.prvがNoneにならない?双方向からの連結を意識。すなわち前からの参照と後ろからの参照双方を書き換える必要がある。
            self.start = self.start.nxt
 
    def delete_last(self):
        if self.start is self.last:
            self.start = self.last = None
        else:
            self.last.prv.nxt = None
            self.last = self.last.prv
 
    def get_content(self):
        #Nodeをリストに変換
        ret = []
        it = self.start
 
        while it is not None:
            ret.append(it.num)
            it = it.nxt
 
        return ' '.join(ret)
 
 
def _main():
    from sys import stdin
 
    n = int(input())
 
    lst = DoublyLinkedList()
     
    for _ in range(n):
        cmd = stdin.readline().strip().split()
        if cmd[0] == 'insert':
            lst.insert(cmd[1])
        elif cmd[0] == 'delete':
            lst.delete_num(cmd[1])
        elif cmd[0] == 'deleteFirst':
            lst.delete_start()
        elif cmd[0] == 'deleteLast':
            lst.delete_last()
 
    print(lst.get_content())
 
 
if __name__ == '__main__':
    _main()