#!/usr/bin/env python

def spam(x, y):
    print(x, y)

spam(10, 20)
spam('wombat', 'bushbaby')
print()

def ham(*args):
    print(args)

ham(1, 2, 3)
ham('a', 'b', 'c')
ham('wombat', 42, None, spam, True, 14.98)
print()

def eggs(p1, p2, *p3):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)

eggs(1, 2, 3, 4, 5)
eggs('a', 'b')
eggs('a', 'b', 'wombat', 'weasel')
print()

def toast(*, bread, spread):
    print("bread:", bread)
    print("spread:", spread)


toast(bread='rye', spread='marmalade')
toast(spread='butter', bread='sourdough')
print()

def config(**kwargs):
    print(kwargs)

config(user='bob', animal='wombat', city='Little Rock')
print()

def big_wacky(arg1, arg2, *args, narg1, narg2, **kwargs):
    pass


def find_stuff(folder='.'):
    print("Searching", folder)


find_stuff()
find_stuff('DATA')

def foo(thing=None):
    if thing is None:
        thing = "default value..."

def bar(*things):
    if len(things):
        print("processing")
    else:
        print("no data")
















