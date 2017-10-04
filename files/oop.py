class Student(object):

    def __init__(self, name, health=100, food="Chips"):
        self.name = name
        self.health = health
        self.food = food

    def __str__(self):
        return "Student Object: {} - {}".format(self.name, self.health)

    def takeTest(self):
        print "{} says \"this test is hard!\"".format(self.name)

    def showFood(self):
        print "{} has {}".format(self.name, self.food)

class Ninja(Student):
    
    default_health = 150
    default_food = "invisible chips"

    @classmethod
    def class_method(cls):
        print "in class method"

    def __init__(self, name, health=default_health, food=default_food):
        super(Ninja, self).__init__(name, health, food)
        

smallNinja = Ninja("Bob")
print smallNinja

Ninja.default_health = 200
print Ninja.default_health

bigNinja = Ninja("Bubu")
print bigNinja

# me = Ninja("Eli", Ninja.default_health, "nice apple")
