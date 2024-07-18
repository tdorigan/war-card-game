class Card:

    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def show(self):
        if not self.is_special():
            print(self.value, "of", self.suit.description.capitalize(), self.suit.symbol)
        else:
            print(Card.SPECIAL_CARDS[self.value], "of", self.suit.description.capitalize(), self.suit.symbol)

    def is_special(self):
        return self.value >= 11
