
from hand import Hand
from deck import Deck
#import hand
#import deck

if __name__=="__main__":

    deck = Deck()
    print deck

    print("*********before shuffle")
    deck.shuffle()
    print deck

    print("*********after shuffle");

    hand1 = Hand()
    deck.move_cards(hand1,5)

    print hand1
