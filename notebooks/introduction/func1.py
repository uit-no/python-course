#!/usr/bin/env python3

langs = ["Perl", "Python", "Java", "Go", "Perl", "Rust", "C++", "Python", "Perl", "Go"]

bad_langs = {"Perl", "C++"}

def count_set(list, set):
    count = 0
    for elem in list:
        if elem in set:
            count += 1
    return count

result = count_set(langs, bad_langs)

print("Level of badness: ", result/len(langs))
