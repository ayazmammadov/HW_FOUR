import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(rank = 12)
        self.assertEqual( card.rank_name, "Queen")
    
    def test_2_club(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_invoke(self):
        card = cards.Card(suit=3, rank = 13)
        #print(card)
        self.assertEqual(str(card), "King of Spades")

    def test_4_invoke(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)
# Check this question 

    def test_5_invoke(self):
        d1=cards.Deck()
        m_card = cards.Card()
        self.assertEqual(type(d1.deal_card()),type(m_card))

# check this question.
    def test_6_deal(self):
        d2= cards.Deck()
        s = len(d2.cards)
        deal = d2.deal_card()
        w = len(d2.cards)
        self.assertEqual(w, 51)
# Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)
   
    def test_7_invoke(self):
        d3=cards.Deck()
        deal_one = d3.deal_card()
        d3.replace_card(deal_one)
        self.assertEqual(len(d3.cards),52)
        
# Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

    def test_8_deck(self):
        d4=cards.Deck()
        lenght_first = len(d4.cards)
        c=cards.Card()
        d4.replace_card(c)
        length_last = len(d4.cards)
        #self.assertEqual(len(d4.cards),52)
        self.assertEqual(lenght_first, length_last)
       
	

# ############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
