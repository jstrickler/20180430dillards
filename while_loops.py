#!/usr/bin/env python

i = 0
while i < 10:
    print(i)
    i += 1

print("Done.")

while True:
    knight_name = input("What is your name? ")
    if knight_name == 'q':
        break
    if knight_name == '':
        continue
    print("OK, {}, off you go!".format(knight_name))
    print()

print()

for i in range(10):
    print(i)
print("Done.")
