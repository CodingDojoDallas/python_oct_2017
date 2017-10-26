# Make 3 Classes and make the classes Interact

#Make a Card Classes

#Make a Deck Classes
#--Reset the Deck
#--Shuffle the Deck
#--Deal cards to players

#Player Classes
#--Name

class Cards(object):
    def __init__(self, suit, number, value):
        self.suit = suit
        self.number = number
        self.value = value

    def suitHearts(self):
        hearts =[]
        self.suit = "Hearts"
        for i in range (1,13):
            if i == 11:
                self.value = 10
            if i ==12:
                self.value =10
            if i ==13:
                self.value = 10
            else:
                self.value = i
            hearts.append(i)
        print hearts
        return hearts
    def suitClubs(self):
        clubs=[]
        self.suit = "Clubs"
        for i in range (1,13):
            if i == 11:
                self.value = 10
            if i ==12:
                self.value =10
            if i ==13:
                self.value = 10
            else:
                self.value = i
            clubs.append(i)
        return clubs
    def suitSpades(self):
        spades=[]
        self.suit = "Spades"
        for i in range (1,13):
            if i == 11:
                self.value = 10
            if i ==12:
                self.value =10
            if i ==13:
                self.value = 10
            else:
                self.value = i
            spades.append(i)
        return spades
    def suitDiamonds(self):
        diamonds=[]
        self.suit = "Diamonds"
        for i in range (1,13):
            if i == 11:
                self.value = 10
            if i ==12:
                self.value =10
            if i ==13:
                self.value =10
            else:
                self.value = i
            diamonds.append(i)
        return diamonds
class Deck(object):
    def __init__(self, cards):
        deck=[hearts, clubs, spades, diamonds]

    def printDeck(self):
        print deck
        return self
class Player(object):
    def __init__(self, name, cards):
        pass

#spades1 = Cards(spades)
Cards.suitHearts(Cards)
