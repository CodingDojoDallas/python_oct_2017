import random

class Card(object):
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def displayInfo(self):
        if self.value == 11:
            print_val = "J"
        elif self.value == 12:
            print_val = "Q"
        elif self.value == 13:
            print_val = "K"
        elif self.value == 14:
            print_val = "A"
        else:
            print_val = str(self.value)
        print print_val +" of "+ self.suit
        return self

class Deck(object):

    def __init__(self):
        self.contents = []
        self.build()

    def build(self):
        self.contents = []
        for i in range(2,15):
            for suit in ["H", "S", "C", "D"]:
                self.contents.append(Card(suit, i))
        self.shuffle()
        return self
        
    def shuffle(self):
        i = len(self.contents)
        while i > 1:
            i -= 1
            j = random.randint(0, i-1)
            self.contents[j], self.contents[i] = self.contents[i], self.contents[j]
        return self
    
    def show_cards(self):
        for card in self.contents:
            card.displayInfo()
        return self

    def draw(self):
        return self.contents.pop()

class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def getCard(self, deck):
        drawn = deck.draw()
        self.hand.append(drawn)
        return self

    def showHand(self):
        if len(self.hand) == 0:
            print "You have no cards!"
        for card in self.hand:
            card.displayInfo()
        return self

    def discard(self):
        self.hand.pop()
        return self

deck = Deck()
deck.show_cards()
print "***********"
player = Player("Jimmy")
player.getCard(deck).showHand().discard().showHand()
print "***********"
deck.show_cards()