class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self

    def riding(self):
        print self.miles + 10
        return self

    def reversing(self):
        print self.miles - 5
        return self


bike1 = Bike(200, "25 mph")
bike2 = Bike(300, "30 mph")
bike3 = Bike(400, "45 mph")

bike1.riding().riding().riding().reversing().displayInfo()
bike2.riding().riding().reversing().reversing().displayInfo()
bike3.reversing().reversing().reversing().displayInfo()
