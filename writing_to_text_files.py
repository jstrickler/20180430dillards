#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

with open('fruitdata.txt', 'w') as fruitdata_out:
    for fruit in fruits:
        rec = '{}\t{}\n'.format(fruit, len(fruit))
        fruitdata_out.write(rec)
