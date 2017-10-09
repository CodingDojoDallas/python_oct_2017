class Animal(object):
    def __init__(self,name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -=1
        return self

    def run(self):
        self.health -=5
        return self
    
    def displayHealth(self):
        print "Your health is {}".format(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name,150) #because you are always 150, this is essentially saying that you're passing "150" into the parent init's health set

    def pet(self):
        self.health += 5
        return self
 
class Dragon(Animal):
    def __init__(self, name): #this is where you tell it what the child should take when calling animal's init method
         super(Dragon,self).__init__(name,170)
    def fly(self):
        self.health -= 10
    def displayHealth(self):
        super(Dragon,self).displayHealth()
        print "I'm a dragon"

''' myanimal = Animal("test",150)
myanimal.walk().walk().walk().run().run().displayHealth() '''
''' snoopdog = Dog("snoop")
snoopdog.walk().walk().walk().run().run().pet().displayHealth() '''
''' mydragon = Dragon("Dany")
mydragon.fly()
mydragon.displayHealth() '''
testanimal = Animal("test2",100)
testanimal.pet()



