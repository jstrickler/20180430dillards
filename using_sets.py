#!/usr/bin/env python

mike_countries = """Italy
France
Germany
Greece
Spain
""".split()

stefan_countries = """Venezuela
Columbia
Canada
Germany
UK
Spain
Russia
""".split()

print(mike_countries)
print(stefan_countries)

mike = set(mike_countries)
stefan = set(stefan_countries)

print("common:", mike & stefan)
print("all:", mike | stefan)
print("only one:", mike ^ stefan)
print("Mike only:", mike - stefan)
print("Stefan only:", stefan - mike)

