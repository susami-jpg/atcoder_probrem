# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:50:00 2021

@author: kazuk
"""

a = [i for i in input().split()]
a.reverse()
stack = []
while a:
    x = a.pop()
    if x == '+':
        s = stack.pop() + stack.pop()
    elif x == '-':
        s = - stack.pop() + stack.pop()
    elif x == '*':
        s = stack.pop() * stack.pop()
    else:
        s = int(x)
    stack.append(s)
    
for i in stack:
    print(i)
    
a = [int(i) for i in input().split()]
n = a[0]
q = a[1]
queu = []
t = 0
for _ in range(n):
    queu.append(input().split)
    
def dequeu():
    return queu.pop(0)
    
def qms(i):
    return int(i[1])
    
def name(i):
    return i[0]

while queu:
    x = dequeu()
    if qms(x) > q:
        qms = qms(x) 
        qms -= q
        queu.append(x)
        t += q
    else:
        qms = qms(x)
        t += qms
        print(f'{name(x)} {t}')
    
        
n = int(input())
newlist = []

for _ in range(n):
    x = input().split()
    if x[0] == 'insert':
        newlist.insert(0, x[1])
    elif x[0] == 'delete':
        if x[1] in newlist:
            newlist.remove(x[1])
    elif x[0] == 'deleteFirst':
        del newlist[0]
    elif x[0] == 'deleteLast':
        del newlist[-1]

print(*newlist)