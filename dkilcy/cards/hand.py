
from deck import Deck

class Hand(Deck):
    """Represents a hand of playing card"""

    def __init__(self, label=""):
        self.cards = []
        self.label = label

if __name__=="__main__":
 
    deck = Deck()
    card = deck.pop_card()

    hand = Hand("new hand")
    hand.add_card(card)

    print hand
