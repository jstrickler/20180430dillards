#!/usr/bin/env python

person = 'Fred', 'Jones', 37

print(person[0])
print(person[0], person[1])

first_name, last_name, age = person

wombats = 'a', 'b', 'c', 'd', 'e', 'f'

x, y, *z = wombats
print(x, y, z)

x, *y, z = wombats
print(x, y, z)

*x, y, z = wombats
print(x, y, z)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'Git'),
]

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print('-' * 60)

print(min(people), max(people))
print(len(people))

nums = [800,80,1000,32,255,400,5,5000]

total = sum(nums)
print(total)

print(sorted(nums))
print()

for i in reversed(nums):
    print(i)
print()


states = ['NC', 'AR', 'CA']
capitals = ['Raleigh', 'Little Rock', 'Sacramento']

sc = zip(states, capitals)

for state, cap in sc:
    print(state, cap)
print()

print(list(zip(states, capitals)), '\n')

for i, cap in enumerate(capitals):
    print(i, cap)

print(list(enumerate(capitals)))

e = enumerate(capitals)
z = zip(states, capitals)
r = reversed(capitals)

print(e, z, r)

print([False] * 10)
print('-' * 60)
print([1,2,3] * 5)
print(['wombat'] * 0)

print([1, 2, 3] + [4, 5, 6])









