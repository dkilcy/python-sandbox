
#import Card
from card import Card
#from hand import Hand

import random

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) 
            
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop() 

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

if __name__ == "__main__":
 
    deck = Deck()
    print deck

    print("*********after shuffle")
    deck.shuffle()
    print deck

