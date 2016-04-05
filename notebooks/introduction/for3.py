#!/usr/bin/env python3

langs = ["Perl", "Python", "Java", "Go", "Perl", "Rust", "C++", "Python", "Perl", "Go"]

bad_langs = {"Perl", "C++"}

bad_counter = 0 

for l in langs:
    if l in bad_langs:
        bad_counter += 1
        if bad_counter > 2:
            print("I quit!!")
            break
        continue 
    print(l)
 
