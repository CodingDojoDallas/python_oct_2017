from random import shuffle

class Card(object):

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def showc(self):
        print "{} of {}".format(self.number, self.suit)


class Deck(object):

    suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.build()

    def build(self):
        self.cards = []
        for suit in self.suits:
            for numbers in self.numbers:
                self.cards.append(Card(suit, numbers))
        self.shuffle()
        return self

    def showd(self):
        for card in self.cards:
            card.showc()
        print "\n"
        return self

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)


class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for idx in range (num):
            self.hand.append(deck.draw())
        return self

    def discard(self, num=1):
        for idx in range(num) :
            self.hand.pop()
        return self

    def showhand(self):
        for card in self.hand:
            card.showc()
        print "\n"
        return self

# card = Card("Spades", "A")
# card.showc()
deck1 = Deck()
# deck1.showd()
# deck1.draw()
# deck1.showd()
player1 = Player('Johnny Chan')
player1.draw(deck1, 5)
player1.showhand()
player1.discard().showhand().draw(deck1, 1).showhand()