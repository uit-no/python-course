#!/usr/bin/env python3

langs = {"Perl", "Python", "Java", "Go", "C++", "Rust"}

bad_langs = {"Perl", "C++"}

for l in langs:
    if l in bad_langs:
        continue 
    print(l)
 
