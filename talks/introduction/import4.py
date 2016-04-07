#!/usr/bin/env python3

import os

result = []

with open('loremipsum', encoding='utf-8') as fil:
    words = fil.read().split()

    for word in words:
        if len(word) > 4:
            if word.endswith(".") or word.endswith(","):
                result.append(word[:-1])
            else:
                result.append(word)

for word in result:
    print(word)




