# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:36:15 2021

@author: kazuk
"""
def main():
    from sys import stdin
    #input = stdin.readline
    from collections import defaultdict
    h, w, m = map(int, input().split())
    bomber = defaultdict(int)
    h_rec = defaultdict(int)
    w_rec = defaultdict(int)
    for _ in range(m):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        bomber[(y, x)] += 1
        h_rec[y] += 1
        w_rec[x] += 1
    
    h_rec = sorted(h_rec.items(), key=lambda x: x[1], reverse=True)
    w_rec = sorted(w_rec.items(), key=lambda x: x[1], reverse=True)
    max_h = h_rec[0][1]
    max_w = w_rec[0][1]
    ans = max_h + max_w
    #bomber = dict(bomber)
    
    flg = 0
    for h_ind, h_score in h_rec:
        if h_score < max_h:
            break
        for w_ind, score in w_rec:
            if score < max_w:
                break
            if not (h_ind, w_ind) in bomber:
                flg = 1
                break
    
    if flg:
        print(ans)
    else:
        print(ans-1)


if __name__ == "__main__":
    main()

    
