# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:39:35 2021

@author: kazuk
"""

import heapq
from sys import exit
from bisect import bisect_left, insort_left

class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        insort_left(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1
            ind = bisect_left(self.h, x)
            self.h.pop(ind)

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]
    
    def get_max(self):
        return self.h[-1]
    
    #HeapDictの中身がなければTrue
    def empty(self):
        if len(self.h) == 0:
            return True
        else:
            return False

#dict型なら複数のHeapDictの集合を扱える
#'key' in dictでkeyの存在を確認できる
H = dict()
H[0] = HeapDict()

#元のHeapDict
import heapq
from sys import exit
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]
    
    #HeapDictの中身がなければTrue
    def empty(self):
        if len(self.h) == 0:
            return True
        else:
            return False
    



