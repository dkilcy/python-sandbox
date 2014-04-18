
class Card(object):
    """Represents a standard playing card"""

    suit_names = ["clubs","diamonds","hearts","spades"]
    rank_names = ["none","ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        #return "%s of %s" % (self.rank, self.suit)
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self,other):
        if self.suit < other.suit:
            return -1
        if self.suit > other.suit:
            return 1
        
        if self.rank < other.rank:
            return -1
        if self.rank > other.rank:
            return 1

        return 0 

    def foo(self):
        pass

#########################################

if __name__ == "__main__":

    card1 = Card(1,12)
    card2 = Card(3,13)

    print("%s" % ( card1 ))
    print("%s" % ( card2 ))

    print(card1 < card2)
