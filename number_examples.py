#!/usr/bin/env python

i1 = 123
i2 = 0b0101
i3 = 0xDeadBeef
i4 = 0o12345

print(i1, i2, i3, i4)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.029039e33

#  complex
#  bool
print('-' * 60)
x = 20
y = 7

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # floored division -- truncate answer to whole number
print(x ** y)
print(x % y)

# x++
# y--

x = 10
x += 5  # x = x + 5
x *= 2  # x = x * 2
x /= 6  # x = x / 6
print(x)

#  x OP= y
#  x = x OP y

# x = 5
# y = x++
# z = ++x


#  int() str() float() bool()

x = "DeadBeef"
print(x * 10)
print(int(x, 16) * 10)



























