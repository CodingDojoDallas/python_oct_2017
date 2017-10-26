class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def display_health(self):
        print self.health
        return self


class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__(name, 150)

    def pet(self):
        self.health = self.health + 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name, 170)

    def fly(self):
        self.health = self.health - 10
        return self

    def display_health(self):
        print self.health + "I am a Dragon"
        return self


animal1 = Animal("Leia", 100)
animal1.walk().walk().walk().run().run().display_health()

dog1 = Dog("Manolo", )
dog1.walk().walk().walk().run().run().pet().display_health()