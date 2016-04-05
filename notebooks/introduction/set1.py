#!/usr/bin/env python3

langs = {"Perl", "Python", "Java", "Go", "C++", "Rust"}

bad_langs = {"Perl", "C++"}

print(langs.difference(bad_langs))

new_langs = {"Rust", "Go", "Dart"}

print(langs.intersection(new_langs))

cool_langs ={"Go", "Python"}

print(cool_langs.issubset(langs))
