#!/usr/bin/env python3

import os


with open('loremipsum', encoding='utf-8') as fil:
    words = fil.read().split()

    for word in words:
        if len(word) > 4:
            print(word)




