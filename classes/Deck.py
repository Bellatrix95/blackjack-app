from classes.Card import Card

#Global variables
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King' )

class Deck:
    '''
    Deck defintion 
    '''
    def __init__(self):
        '''
        Adds cards to the deck
        '''
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

