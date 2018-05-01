#!/usr/bin/env python

# with EXPR:
# with EXPR as VAR:
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\r\n')
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(contents)
    print('=' * 30)
    print(repr(contents))

print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    lines = (line.rstrip() for line in mary_in)
    for line in lines:
        print(line)














