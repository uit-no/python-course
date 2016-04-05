#!/usr/bin/env python3

langs = ["Perl", "Python", "Java", "Go", "Perl", "C++", "Rust", "Python", "Perl", "Go"]

bad_langs = {"Perl", "C++"}

bcounter = 0 

for l in langs:
    if l in bad_langs:
        bcounter ++
        continue 
    print(l)
 
