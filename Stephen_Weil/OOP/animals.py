class Animal(object):

    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def __repr__(self):
        return "<Animal object {}, {} health>".format(self.name, self.health)
    
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def display_health(self):
        print "Current health of " + self.name + ": " + str(self.health)
        return self

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):

    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        super(Dragon, self).display_health()
        print "I AM A DRAGON!! I WILL BURNINATE THE COUNTRYSIDE!!"
        return self

if __name__ == "__main__":
    fox = Animal("fox")
    fox.walk().walk().walk().run().run().display_health()

    golden = Dog("Golden Retriever")
    golden.walk().walk().walk().run().run().pet().display_health()

    trogdor = Dragon("Trogdor the Burninator")
    trogdor.fly().fly().display_health()

# these should fail
    notadragon = Animal("Not a dragon")
# notadragon.fly() - returns "'Animal' object has no attribute fly"
    notadragon.display_health() # just returns health (at 100, not 170) with no message

# golden.fly() - returns " 'Dog' object has no attribute fly"