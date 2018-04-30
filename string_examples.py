#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"


print("Python's the bomb!")
print('A "python" thing')

print("A \"python\" thing")  # DO NOT DO THIS

print("""It's a "Python" thing!""")

query = """
select * 
from ytd_sales
where region = 'SE'
order by store desc
"""

print("spam\\n")  # DO NOT DO THIS
print(r"spam\n")  # DO THIS
print()

cave_man = 'Barney Rubble'

print(len(cave_man))

print(cave_man.upper())
cave_man.upper()
print(cave_man)

print(cave_man.count('b'))
print(cave_man.count('Rub'))
print(cave_man.count('Poke'))
print(cave_man.lower().count('b'))

record = 'fee:fi:fo:fum'
fields = record.split(':')
print(fields)

data = 'apple mango guava kiwi     pear  peach pomegranate'

fruits = data.split()
print(fruits)
print()

print(cave_man.startswith('Foo'))
print(cave_man.startswith('Bar'))

print("ub" in cave_man)
print('bu' in cave_man)
print()


s1 = "        All my exes live in Texas          "
print("|" + s1.lstrip() + "|")
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")
print()

s2 = "xyxxyyxxxyyyAll my exes live in Texasyxyyxxyyyxxx"
print("|" + s2.lstrip('xy') + "|")
print("|" + s2.rstrip('xy') + "|")
print("|" + s2.strip('xy') + "|")
print()

x = "Little"
y = "Rock"

city = x + " " + y
print(city)


