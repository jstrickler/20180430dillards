#!/usr/bin/env python

import os

os.system('netstat -an')

print('-' * 60)

with os.popen('netstat -an') as netstat_in:
    for line in netstat_in:
        if "ESTABLISHED" in line:
            print(line.rstrip())


with os.popen('netstat -an') as netstat_in:
    output = netstat_in.read()


