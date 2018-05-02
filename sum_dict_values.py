#!/usr/bin/env python


d = {'foo': '7', 'bar': '9', 'blah': '3'}

total = sum([int(v) for k, v in d.items()])

print(total)

print(list(d.keys())[0])
print(list(d.keys())[2])
