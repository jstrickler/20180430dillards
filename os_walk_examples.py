#!/usr/bin/env python

import os

TARGET = '.'

for curr_dir, dir_list, file_list in os.walk(TARGET):
    if 'git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print('    {:6d} {}'.format(file_size, file_name))
