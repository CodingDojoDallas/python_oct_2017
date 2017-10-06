class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def walk(self):
        self.health-=1
        return self

    def run(self):
        self.health-=5
        return self

    def displayhealth(self):
        print ""
        print self.name + " has " + str(self.health) + " health "
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
        
    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name,170)

    def fly(self):
        self.health-=10
        return self

    def displayhealth(self):
        super(Dragon,self).displayhealth()
        print "I am a Dragon hear me ROAR!"
        return self

anim1 = Animal("Cat", 100)
anim1.walk().walk().walk().run().run().displayhealth()

anim2 = Dog("Rover")
anim2.walk().walk().walk().run().run().pet().displayhealth()

anim3 = Dragon("Puff")
anim3.fly().displayhealth()