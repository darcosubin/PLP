from random import shuffle

class Cards(object):
    pcard=[]
    def __init__(self,name):
        "Initialize a deck of 52 cards, also contains back cover"
        self.name=name
        start=127136
        end=127198 #not :127167, 127183,127199
        kard=range(start,end)
        for cards in kard:
            self.pcard.append(cards)
    
    def shuffle(self):
        shuffle(self.pcard)

    def card(self):
        "removes a card from the deck, and returns it"
        if len(self.pcard) > 0:
            return unichr(self.pcard.pop())
        return None
    
    def __str__(self):
        return u"A deck of {}".format(self.name)

if __name__=='__main__':
    print ("Getting a deck of cards...")
    cards = Cards("Bycicle")
    print cards
    print "Shuffling cards..."
    cards.shuffle()
    print (
        u"Get a card: {}".format(
            cards.card()
        )
    )
