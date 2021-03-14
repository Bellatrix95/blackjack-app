import random

class Dealer:
    '''
    Dealer defintion 
    '''
    
    def __init__(self, deck):
        '''
        Deck object should be passed as an argument so the dealer could handle changes on it
        '''
        self.deck = deck
        self.shuffle()
        self.cards = []

    def deal(self, cards):
        '''
        Save multiple cards
        '''
        self.cards.extend(cards)

    def hit(self):
        '''
        Save a card
        '''
        self.cards.append(self.deal_one())

    def check_sum(self):
        '''
        Check cards values sum
        '''
        sum_values = 0
        for card in self.cards:
            sum_values += card.value
        return sum_values

    def shuffle(self):
        '''
        Shuffle the deck
        '''
        random.shuffle(self.deck.cards)

    def deal_one(self):
        return self.deck.cards.pop()

    def show_cards(self):
        print("Dealer has : ")
        for card in self.cards:
            print(card)

    def show_cards_sum(self):
        print("Dealer has carts value " + str(self.check_sum()))
