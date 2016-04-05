#!/usr/bin/env python3

import os

x = 4

with open('loremipsum', encoding='utf-8') as fil:
    words = fil.read().split()

    for w in words:
        if len(w) > x:
            print(w)




