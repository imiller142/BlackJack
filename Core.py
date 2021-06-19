import random

SUITS = ('Clubs', 'Diamonds', 'Spades', 'Heats')
RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
VALUE = {'Ace': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    # Will return value of card
    def __str__(self):
        return self.rank + ' of ' + self.suit
        

#deck will take cards
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                return self.deck.append(Card(suit, rank))

    def __str__(self):
        pass
    
class Player:
    
    def __init__(self,name):
        self.name = name

    def bank(self):
        pass
        

    
class Hand(Deck):
    pass

playerOne = Player()

playerOne.get_name

