from poker.game.card import Card
from poker.game.deck import Deck
from poker.game.game_round import GameRound
from poker.game.hand import Hand
from poker.game.player import Player
from flask_login import current_user

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "Bot", hand = hand1)
player2 = Player(name = current_user, hand = hand2)
players = [player1, player2]

game_round = GameRound(deck = deck, players = players)
game_round.play()

@property
def show_rank():
    for player in players:
        # print(f"{player.name} receives a {player.hand}.")
        index, hand_name, hand_cards = player.best_hand()
        hand_cards_strings = [str(card) for card in hand_cards]
        hand_cards_string = " and ".join(hand_cards_strings)
        return (f"{player.name} has a {hand_name} with a {hand_cards_string}.")

@property
def show_winner():
    winning_player = max(players)
    return (f"The winner is {winning_player.name}.")

@property
def show_hand():
    for player in players:
        return (f"{player.name} receives a {player.hand}.")