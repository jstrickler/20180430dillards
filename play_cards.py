#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Aggie")

print(d1)

print(d1.dealer)

d1.dealer = 'Bob'

print(d1.dealer)

try:
    d1.dealer = 123
except TypeError as err:
    print(err)


print(d1.cards)
print()

d1.shuffle()
print(d1.cards, '\n')

d2 = CardDeck('Mary')
d3 = CardDeck("Jose")

print(d1.get_suits())

print(CardDeck.get_suits())

j1 = JokerDeck('Billy')
print(j1)
j1.shuffle()
print(j1.cards, '\n')
