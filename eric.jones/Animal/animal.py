class Animal(object):

    name = ""
    health = 0

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayhealth(self):
        print "Health: {}\n".format(self.health)
        return self

class Dog(Animal):

    def __init__(self):
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):

    def __init__(self):
        self.health = 170

    def fly(self):
        self.health -=10
        return self

    def displayhealth(self):
        super(Dragon, self).displayhealth()
        print "I am Dragon"
        return self


animal = Animal()
animal.walk().walk().walk().run().run().displayhealth()
dog = Dog()
dog.walk().walk().walk().run().run().pet().displayhealth()
dragon = Dragon()
dragon.fly().walk().displayhealth()