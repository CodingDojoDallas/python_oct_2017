class Animal(object):
    """docstring for Animal."""
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def dispHealth(self):
        print "Name: {} | Health: {}".format(self.name, self.health)
        return self

class Dog(Animal):
    """docstring for Dog."""
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def fly(self):
        self.health -+ 10
        return self

    def dispHealth(self):
        super(Dragon, self).dispHealth()
        print "I am Blue Eyes White Dragon!!!"
        return self

animal1 = Animal("Elephant", 160)
animal1.walk().walk().walk().run().run().dispHealth()

dog1 = Dog("Marmaduke")
dog1.walk().walk().walk().run().run().pet().dispHealth()

dragon1 = Dragon("Blue Eyes White Dragon")
dragon1.fly().dispHealth()

brokendog = Dog("I can't fly!")
# Class Dog does not have the ability to fly because it is not a dragon and has no method called fly
brokendog.walk().run().pet().fly().dispHealth()

unfriendlydragon = Dragon("I will eat you if you try to pet me, foolish human...")
# Class Dragon cannot be pet because it is not a dog and has no method called pet
dragon1.fly().pet().dispHealth()

angryanimal = Animal("DON'T YOU F**KIN PET ME!", 200)
# Class Animal cannot be pet (or fly) because it is not a dog or dragon and has no method called pet or fly
angryanimal.walk().run().pet().fly().dispHealth()
