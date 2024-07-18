class WarCardGame:

    # constants to identify the winner
    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._full_deck = deck

        # When creating an instance of the game, make the decks
        self.make_initial_decks()

    def make_initial_decks(self):
        self._full_deck.shuffle()  # shuffles the full deck
        self.make_deck(self._player)  # get/draw half of the deck
        self.make_deck(self._computer)  # get the other half

    def make_deck(self, character):
        for i in range(26):  # 26 cards is half of the full deck, it's gonna be half for each player
            card = self._full_deck.draw()
            character.add_card(card)

    # main logic of the game
    # 2 main stages: BATTLE (the normal round) and WAR (when there's a tie in the battle)
    def start_battle(self, cards_from_war=None):

        print("\n== Let's Start the Battle ==\n")

        player_card = self._player.draw_card()
        #  if the player has no card to draw, computer wins
        if player_card is None:
            return WarCardGame.COMPUTER

        computer_card = self._computer.draw_card()
        #  if the computer has no card to draw, player wins
        if computer_card is None:
            return WarCardGame.PLAYER

        print(f"Your Card: ")
        player_card.show()

        print(f"\nComputer Card: ")
        computer_card.show()
        
        # check round's winner
        winner = self.get_round_winner(player_card, computer_card)
        # get list of cards won
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won this round.")
            self.add_cards_to_character(self._computer, cards_won)
        else:  # TIE
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif computer_card.value > player_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, computer_card, previous_cards):
        """Return list of the cards won: player card + computer card + war (previous) cards if they exist"""
        if previous_cards:  # if previous_cards is not empty
            # player and computer cards are cards objects, we make a list with them, and then concatenate with
            # previous cards, which is another list of cards
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character, cards_won):
        for card in cards_won:
            character.add_card(card)

    def start_war(self, cards_from_battle):

        # list of 3 cards for each player that will be drawn and put to the war
        player_cards = []
        computer_cards = []

        for i in range(3):
            # get the 3 cards for each character
            player_card = self._player.draw_card()
            #  if the player has no card to draw, computer wins
            if player_card is None:
                return

            computer_card = self._computer.draw_card()
            #  if the computer has no card to draw, player wins
            if computer_card is None:
                return

            # add them to the list
            player_cards.append(player_card)
            computer_cards.append(computer_card)

        print("Six hidden cards: XXX XXX")

        # we pass the 3 cards from each character + the cards from the previous battle
        # and star a battle again
        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("===========================================")
            print("                 Game Over                 ")
            print("        The Computer won. Try again.       ")
            print("===========================================")
            return True
        elif self._computer.has_empty_deck():
            print("===========================================")
            print(f"          Congratulations {self._player.name}    ")
            print("                  You won!                 ")
            print("===========================================")
            return True
        else:
            return False

    def print_stats(self):
        print("\n----")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"The Computer has {self._computer.deck.size} cards on its deck.")
        print("----")

    def print_welcome_message(self):
        print("===========================================")
        print("       Welcome to the War Card Game!       ")
        print("===========================================")


