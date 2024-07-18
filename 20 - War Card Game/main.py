from deck import Deck
from player import Player
from war_card_game import WarCardGame

# player and computer with empty decks
player = Player("Player", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
# not empty deck
deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():

    answer = input("\nPress any key to continue or Q to quit\n")
    if answer.lower() == "q":
        print("Game Over")
        break

    game.start_battle()
    game.print_stats()

