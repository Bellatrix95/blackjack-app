class Player:
    '''
    Player defintion 
    '''
    def __init__(self):
        self.cards = []

    def deal(self, cards):
        '''
        Save multiple cards
        '''
        self.cards.extend(cards)

    def hit(self, card):
        '''
        Save one cards
        '''
        self.cards.append(card)

    def check_sum(self):
        '''
        Check cards values sum
        '''
        sum_values = 0
        for card in self.cards:
            sum_values += card.value
        return sum_values

    def show_cards(self):
        print("Player has : ")
        for card in self.cards:
            print(card)
    
    def clear_cards(self):
        '''
        Clears cards array
        '''
        self.cards = []

    def show_cards_sum(self):
        print("Player has carts value " + str(self.check_sum()))
