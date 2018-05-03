#!/usr/bin/env python
import random


class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._cards = None
        self.dealer = dealer
        self._create_deck()


    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = '{}-{}'.format(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    def deal(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    @property
    def dealer(self):
        return self._dealer.upper()

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_suits(cls):
        return cls.SUITS
