import random

from card import Card
from suit import Suit


class Deck:

    SUITS = ("clubs", "diamonds", "hearts", "spades")

    def __init__(self, is_empty=False):
        # the first card in the list is the BOTTOM of the deck, the last is the TOP
        self._cards = []
        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        """Build a 52 cards deck: 13 cards for each of the 4 suits"""
        #  for suit in Suit.SYMBOLS:  # the 4 possible suits
        for suit in Deck.SUITS:  # the 4 possible suits
            for value in range(2, 15):  # from 2 to 14 inclusive
                self._cards.append(Card(Suit(suit), value))

    def show(self):
        """Show all the deck's cards"""
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):  # take a card from the dek - O FAMOSO PESCAR
        # the first card in the list is the BOTTOM of the deck, the last is the TOP
        if self._cards:  # if the list is not empty
            return self._cards.pop()  # removes and return the last (TOP) element of the list
        else:
            return None  # return something always, not only if it's true

    def add(self, card):
        #  inserts at the BOTTOM/beginning of the deck
        self._cards.insert(0, card)
