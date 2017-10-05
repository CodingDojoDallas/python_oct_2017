class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self, times):
        self.health -= (times * 1)
        return self

    def run(self, times):
        self.health -= (times * 5)
        return self

    def displayHealth(self):
        print self.name
        print self.health

animal1 = Animal("Gizmo", 15)
animal1.walk(3).run(2).displayHealth()

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health=150)

    def pet(self, times):
        self.health += (times * 5)
        return self

dog1 = Dog("Gizmo")
dog1.walk(3).run(2).pet(1).displayHealth()
