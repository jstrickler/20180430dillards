#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

def ignore_case(fruit):
    return fruit.lower()

f1 = sorted(fruits, key=ignore_case)
print("f1:", f1, '\n')

x = 'RUTABAGA'
print(str.lower(x), '\n')

f2 = sorted(fruits, key=str.lower)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def my_sort(e):
    return len(e), e.lower()

f4 = sorted(fruits, key=my_sort)
print("f4:", f4, '\n')

f4lam = sorted(fruits, key=lambda e: (len(e), e.lower()))
print("f4lam:", f4lam, '\n')


def my_sort_kathy(e):
    return e.lower(), len(e)

f5 = sorted(fruits, key=my_sort_kathy)
print("f5:", f5, '\n')


x = [1, 5, 'wombat', None, "None", True, 81.73]

x1 = sorted(x, key=str)
print("x1:", x1, '\n')

nums = [800,80,1000,32,255,400,5,5000]

n1 = sorted(nums, key=str)
print("n1:", n1, '\n')

def sort_stefan(n):
    s = str(n)
    return len(s), s

n2 = sorted(nums, key=sort_stefan)
print("n2:", n2, '\n')


#  max() min()

print(max(fruits))
print(max(fruits, key=str.lower))


print(sorted(nums, reverse=True))



fruits.sort(key=str.lower)
print(fruits)
