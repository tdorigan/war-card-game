class Player:

    def __init__(self, name, deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer

    @property
    def deck(self):
        return self._deck

    @property
    def is_computer(self):
        return self._is_computer

    def has_empty_deck(self):
        return self.deck.size == 0

    def draw_card(self):
        if not self.has_empty_deck():
            return self.deck.draw()
        else:
            return None

    def add_card(self, card):
        self.deck.add(card)
