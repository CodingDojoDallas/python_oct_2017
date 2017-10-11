class Card(object):
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
    def show(self):
        print "{} of {}".format(self.number,self.suit)
        return self

class Deck(object):
    def __init__(self):
        self.deck = []
        self.build()
    def build(self):
        for i in range(0,2):
            self.deck.append(Card("2", "Hearts"))
        return self
    def showUrD(self):
        for card in self.deck:
            card.show()
        return self
    def topCard(self):
        self.deck.pop(self.deck[0])
        print self.deck.pop(self.deck[0])
        return self
    def shuffle(self):  #DO LAST
        pass

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = [] 
    def draw(self,deck): #draw to hand, from deck, ???x amount of times???
        topCard(self.deck)
        return self
    def discard(self): #discard to self.deck
        pass
    def show(self):
        for card in self.hand:
            card.show()

card1 = Card("A", "Clubs")
card1.show()
deck = Deck().build().showUrD()
player1 = Player("Remy")
player1.draw(deck).show()