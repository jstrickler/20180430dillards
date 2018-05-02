#!/usr/bin/env python

x = 5

def spam():
    y = 100
    print("Hello, x is", x)
    return y


pink_wombat = spam()
print("return_value is", pink_wombat)

print(5 + spam())


def double_it(x):
    return x * 2


print(double_it(5))
print(double_it(3.4903))
print(double_it("GO"))


