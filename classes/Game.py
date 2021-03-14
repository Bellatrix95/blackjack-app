from classes.Player import Player
from classes.Dealer import Dealer
from classes.Deck import Deck

class Game:
    '''
    Blackjack game ame logic 
    '''

    def __init__(self, num_of_rounds = 5):
        self.num_of_rounds = num_of_rounds
        self.player = Player()
        self.dealer = Dealer(Deck())
        self.dealer_won = 0
        self.player_won = 0
        self.draw = 0
 
    def player_won_stats(self):
        self.player_won += 1

    def dealer_won_stats(self):
        self.dealer_won += 1
    
    def draw_stats(self):
        self.draw += 1

    def start_round(self):
        '''
        Runs defined number of rounds. Default is 5 rounds of Blackjack.
        '''
        for round in range(self.num_of_rounds):
            self.player.clear_cards()
            self.start_game()

    def deal(self):
        '''
        Handles initial deal logic for the dealer and one player.
        '''
        deal_player = []
        deal_dealer = []
        for deal_card in (1,2):
            deal_player.append(self.dealer.deal_one())
            deal_dealer.append(self.dealer.deal_one())

        self.player.deal(deal_player)
        self.dealer.deal(deal_dealer)
        
            
    def start_game(self):
        '''
        Handles Blackjack game logic for the dealer and one player.
        '''

        #defined again so the Deck with 52 cards is used
        self.dealer = Dealer(Deck())
        
        self.deal()

        #the player automatically hits if the cards value sum is less than 17
        while self.player.check_sum() < 17:
            self.player.hit(self.dealer.deal_one())

            #if the cards value sum is greater than 21, the player lost
            if self.player.check_sum() > 21:
                self.dealer_won_stats()
                return

        #if the dealer has two aces, he lost
        if self.dealer.check_sum() == 22:
            self.player_won_stats()
            return

        #if the dealer has a higher value than the player, he won
        if self.dealer.check_sum() > self.player.check_sum():
            self.dealer_won_stats()
            return
        
        #the dealer automatically hits if the cards value sum is less than player's
        while self.dealer.check_sum() < self.player.check_sum():
            self.dealer.hit()

            #if the dealer's cards value sum is greater than 21, the dealer lost
            if self.dealer.check_sum() > 21:
                self.player_won_stats()
                return
            
            #if the dealer has a higher value than the player, he won
            if self.dealer.check_sum() > self.player.check_sum():
                self.dealer_won_stats()
                return

        #if the dealer and the player have the same cards value sum, it's a draw
        if self.player.check_sum() == self.dealer.check_sum():
            self.draw_stats()
            return

    def __str__(self):
        return f"The simulator ran {self.num_of_rounds} times \n" +  f"The player won {self.player_won} times \n" + f"The dealer won {self.dealer_won} times \n" + f"There were {self.draw} draws"