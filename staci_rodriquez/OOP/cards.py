class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        

    def show(self):
        print "{} of {}".format(self.value, self.suit) 
        return self


class Deck(object):
    def __init__(self):    
        self.card = []
        self.build()

    def build(self):
        
        return self

    def show(self):

    def draw(self):

    def shuffle(self):   
        print "shuffled"



# class Person(object):
#     def __init__(self, name, hand):
#         self.name = "Bob"
        

#     def deck(self, ):


card1 = Card("hearts", 3)
card1.show()
deck1 = Deck()

