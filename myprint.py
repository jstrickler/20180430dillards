#!/usr/bin/env python
import sys

def my_print(*args, sep=' ', end='\n'):
    for arg in args[:-1]:
        sys.stdout.write(str(arg))
        sys.stdout.write(sep)
    sys.stdout.write(str(args[-1]))
    sys.stdout.write(end)

