VALUES = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
            'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Card:
    '''
    Card suit, rank and value definition
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
