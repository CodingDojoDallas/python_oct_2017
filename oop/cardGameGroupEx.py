class Card(object):
    """docstring for Card."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "[{},{}]".format(self.suit, self.value)

    def showCard(self):
        print self

# card1 = Card("a", "1")
# card2 = Card("a", "2")
# card1.showCard()
# card2.showCard()

class Deck(object):
    """docstring for Deck."""
    def __init__(self):
        self.deck = []
        self.buildDeck()

    def __str__(self):
        return "Deck: {}".format(self.deck)

    def buildDeck(self):
        for suit in ["a","b","c","d"]:
            for value in range(1, 14):
                newCard = Card(suit, value)
                self.deck.append(newCard)

    def showDeck(self):
        for card in self.deck:
            card.showCard()
        return self

deck1 = Deck().showDeck()

class Player(object):
    """docstring for Player."""
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return "Deck: {}".format(self.deck)

    def showHand():


    def drawCard():
