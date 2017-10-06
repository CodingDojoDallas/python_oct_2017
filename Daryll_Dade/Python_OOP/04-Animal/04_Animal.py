class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        print "Walk"
        print "{} health decreased by 1".format(self.name)
        return self

    def run(self):
        self.health -= 5
        print "Run"
        print "{} health decreased by 5".format(self.name)
        return self

    def display_health(self):
        print "{} has {} health.".format(self.name, self.health)
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
        print "{}'s health is {}.".format(self.name, self.health)


    def pet(self):
        print "pet"
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
        print "I am a Dragon...If you culden't tell. Name: {}   Health:{}".format(self.name, self.health)


    def fly(self):
        print "fly"
        self.health -=10
        return self

# test =Animal('spot', 100)
animal = Animal('animal1', 150)
animal2 = Animal('animal2', 150)
#dog3 = Animal(Dog, 100)
# dragon = Dragon( 170)
dog1 = Dog('spike',10)
dog2 =Dog('Woofie', 0)
greygor = Dragon('Greygor', 100)


dog1.walk().walk().walk().run().run().pet().display_health()
greygor.fly().fly().display_health()
dog2.pet().display_health()

# dog2.pet().display_health()
# dragon.fly()
# print test.name
# print test.health
#spot.display_health()
# print Dog.health
#print x
