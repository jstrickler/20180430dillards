#!/usr/bin/env python

d1 = dict()
d2 = {'red': 5, 'green': 6, 'black': 3, 'pink': 14}
d3 = {}
d4 = dict(red=5, green=6, black=3, pink=14)

print(len(d4))
print(d4['red'])
print(d4['pink'])

key = 'orange'
if key in d4:
    print(d4[key])

print(d4.get(key))
print(d4.get(key, -1))

print(d4.setdefault(key, 10))

print(d4)

other_colors = {'green': 17,
    'brown': 5, 'teal': 18, 'a sort of reddish mauve': 8
}


# d4.update(other_colors)
print(d4)


[d4.setdefault(k, v) for k, v in other_colors.items() if k not in d4]
print(d4)



for color, value in d4.items():
    print(color, value)
print()


for color, value in sorted(d4.items()):
    print(color, value)
print()




