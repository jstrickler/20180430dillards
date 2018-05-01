#!/usr/bin/env python


counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        item = raw_line.rstrip()
        if item not in counts:
            counts[item] = 0

        counts[item] = counts[item] + 1
        # counts[item] += 1

print(counts)
