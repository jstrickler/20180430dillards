#!/usr/bin/env python

import os  # auto-imports os.path
from datetime import datetime

FOLDER = 'DATA'
FILE = 'mary.txt'

file_path = os.path.join(FOLDER, FILE)

print("file path:", file_path, '\n')

with open(file_path) as mary_in:
    contents = mary_in.read()
    print(contents, '\n')

file_size = os.path.getsize(file_path)
print('file size:', file_size)

print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.abspath(file_path))

raw_timestamp = os.path.getmtime(file_path)
print('raw timestamp', raw_timestamp)

timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)

stat_info = os.stat(file_path)
print(stat_info)







