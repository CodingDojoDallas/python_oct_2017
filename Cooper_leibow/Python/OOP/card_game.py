class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def displayInfo(self):
        print self.suit + str(self.value)
        return self

class Deck(object):

class Player(object):
    def __init__(self, name,):
        self.name = name
        self.hand = []

    def getCard(self, deck):
        drawn = deck.draw()
        self.hand.append(drawn)
        return self
