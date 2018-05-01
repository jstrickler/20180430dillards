#!/usr/bin/env python


with open('fruitdata.txt') as fruitdata_in:
    with open('fruitdata_new.txt', 'w') as fruitdata_out:
        for line in fruitdata_in:
            fruit, length = line.rstrip().split('\t')
            new_rec = '{},{}\n'.format(fruit.upper(), length)
            fruitdata_out.write(new_rec)

