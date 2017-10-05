class Animal(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def walk(self):
        self.hp -= 1
        return self

    def run(self):
        self.hp -= 5
        return self

    def display(self):
        print "HP: " + str(self.hp)
        return self

animal1 = Animal("Leo", 40)
animal1.walk().walk().walk().run().run().display()

class Dog(Animal):
    def __init__(self, name, hp):
        super(Dog, self).__init__(name, hp)
        self.hp = 150

    def pet(self):
        self.hp += 5
        return self

dog1 = Dog("Zorro", 5)
dog1.walk().walk().walk().run().run().pet().display()

class Dragon(Animal):
    def __init__(self, name, hp):
        super(Dragon, self).__init__(name, hp)
        self.hp = 170

    def fly(self):
        self.hp -= 10
        return self

    def display(self):
        super(Dragon, self).display()
        print "I AM A DRAGON! RAWRrrRrr"
        return self

dragon1 = Dragon("Smaug", 2)
dragon1.walk().walk().run().run().fly().display()

animal2 = Animal("z", 30)
#animal2.walk().pet()
#animal2.walk().fly()

dog2 = Dog("ade", 32)
#dog2.fly()

dragon2 = Dragon("Mushu", 1)
#dragon2.pet()