#!/usr/bin/env python

fruits = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'kiwi', 'lime']

print(fruits[0], fruits[2], fruits[-1])
print(len(fruits))
fruits.append('grapefruit')
fruits.append('papaya')
fruits.append('peach')

print(fruits, '\n')

print(fruits[0:3], '\n')
print(fruits[:3], '\n')
print(fruits[2:6], '\n')
print(fruits[5:len(fruits)])
print(fruits[5:])
print(fruits[-3:])
print(fruits[5:98])

city = 'Little Rock'

print(city[:3])
print(city[-4:])
print(city[7:9])

print(fruits)

fruits[2:4] = ['pomegranate', 'lemon', 'raspberry', 'marionberry']
print(fruits, '\n')

for fruit in fruits:
    print(fruit)

print('-' * 60)

for letter in city:
    print(letter)

print()
print(fruits)
every_other = fruits[::2]
print(every_other)
print(fruits[len(fruits):0:-1])
