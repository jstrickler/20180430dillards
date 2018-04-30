#!/usr/bin/env python

s1 = "hello"   # string, can be Unicode

b1 = b"hello"  # bytes, must be encoded to Unicode

print(s1.encode())
print(b1.decode())

# ---------

x = 5
y = 10
z = 'abc'

print(x, y, z)
print("pastafazool")


print(x, y, z, sep='/')
print(x, y, z, sep=', ')
print(x, y, z, sep=' <==> ')
print(x, y, z, sep='')

print("one", end=':')
print("two", end=';')
print("three", end='\n\n')
print("four")

