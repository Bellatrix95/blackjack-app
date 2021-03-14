import unittest
from classes.Deck import Deck
from classes.Card import Card
from classes.Player import Player
from classes.Dealer import Dealer
from classes.Game import Game

class CardTest(unittest.TestCase):
    
    def test_card_value(self):
        suit = 'Hearts'
        rank = 'Ace'
        result = Card(suit, rank)
        self.assertEqual(result.value, 11)

class DeckTest(unittest.TestCase):
    
    def test_create_deck(self):
        result = Deck()
        self.assertEqual(len(result.cards), 52)

class DealerTest(unittest.TestCase):
    
    def test_deal_one(self):
        dealer = Dealer(Deck())
        card = dealer.deal_one()
        self.assertIsInstance(card, Card)
    
    def test_check_cards_value_sum(self):
        dealer = Dealer(Deck())
        card1= dealer.deal_one()
        card2 = dealer.deal_one()
        cards_value_sum = card1.value + card2.value
        dealer.deal([card1, card2])
        self.assertEqual(dealer.check_sum(), cards_value_sum)

class PlayerTest(unittest.TestCase):
    
    def test_hit(self):
        dealer = Dealer(Deck())
        card = dealer.deal_one()
        player = Player()
        player.hit(card)
        self.assertListEqual(player.cards, [card])

    def test_check_cards_value_sum(self):
        dealer = Dealer(Deck())
        player = Player()
        card1= dealer.deal_one()
        card2 = dealer.deal_one()
        cards_value_sum = card1.value + card2.value
        player.deal([card1, card2])
        self.assertEqual(player.check_sum(), cards_value_sum)

class GameTest(unittest.TestCase):
    
    def test_default_num_of_round(self):
        game = Game()
        self.assertEqual(game.num_of_rounds, 5)

    def test_deal_logic(self):
        game = Game()
        game.deal()
        self.assertEqual(len(game.dealer.cards), 2)
        self.assertEqual(len(game.player.cards), 2) 

if __name__=='__main__':
    unittest.main()