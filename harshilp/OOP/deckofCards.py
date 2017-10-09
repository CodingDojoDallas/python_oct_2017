from random import shuffle
class Card(object):
    def __init__ (self, suit, value):
        self.suit = suit
        if value == 1:
            self.value = "Ace"
        elif value == 11:
            self.value = "Jack"
        elif value == 12:
            self.value = "Queen"
        elif value == 13:
            self.value = "King"
        else:
            self.value = value
        
    def showInfo(self):
        print str(self.value) + " of " + self.suit

#card1 = Card("Spade", 7)
#card1.showInfo()

class Deck(object):
    def __init__ (self):
        self.cardList = []
        self.discardPile = []
        self.initialize()

    def initialize(self):
        self.cardList = []
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
        for suit in suits:
            for val in range(1,14):
                self.cardList.append(Card(suit, val))

    def showList(self):
        for card in self.cardList:
            card.showInfo()

    def draw(self):
        card = self.cardList.pop()
        card.showInfo()
        return card

    def shuffle(self):
        shuffle(self.cardList)

deck1 = Deck()
deck1.showList()
#deck1.shuffle()
#deck1.showList()
#deck1.draw()
#deck1.showList()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def drawCard(self, deck):
        print "You drew: "
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        print "Your Hand contains: "
        for i in self.hand:
            i.showInfo()

    def shuffle(self, deck):
        deck.shuffle()

player1 = Player("Harshil")
player1.drawCard(deck1)
player1.showHand()
player1.shuffle(deck1)
player1.drawCard(deck1).showHand()
