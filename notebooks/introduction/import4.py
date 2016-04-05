#!/usr/bin/env python3

import os

x = 4
res = []

with open('loremipsum', encoding='utf-8') as fil:
    words = fil.read().split()

    for w in words:
        if len(w) > x:
            if w.endswith(".") or w.endswith(","):
                res.append(w[:-1])
            else:
                res.append(w)

for w in res:
    print(w)




