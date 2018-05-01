#!/usr/bin/env python

list1 = list() # <1>
list2 = ['apple', 'banana', 'mango']  # <2>
list3 = []  # <3>
list4 = 'apple banana mango'.split()  # <4>

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("list4:", list4)

print("list2[0]:", list2[0])   # <5>
print("list4[2]:", list4[2])   # <6>

print("list4[-1]:", list4[-1]) # <7>
print()

fruits = 'apple banana mango'.split()

print(fruits)
fruits.append('orange')
print(fruits)
# fruits.append(1)
# fruits.append(None)
# fruits.append(392.2903)

more_fruits = ['kiwi', 'lime', 'fig']

fruits.extend(more_fruits)
print(fruits)

fruits.insert(0, 'papaya')
fruits.insert(4, 'durian')

print(fruits)

fruits[4] = 'strawberry'

print(fruits)

print('orange' in fruits)
print(fruits.index('orange'))
fruits.insert(0, 'orange')
fruits.append('orange')
fruits.append('orange')
print(fruits)

locations = []
pos = -1
while True:
    try:
        pos = fruits.index('orange', pos + 1)
    except ValueError:
        break
    locations.append(pos)

print(locations)


locations = [i for i, fruit in enumerate(fruits) if fruit == 'orange']
print(locations)

del fruits[-1]
del fruits[-1]
del fruits[0]

print(fruits)

f1 = fruits.pop()
print(f1)
print(fruits, '\n')

f2 = fruits.pop(0)
print(f2)
print(fruits, '\n')

print(f1, f2, '\n')

fruits.remove('lime')

print(fruits)


