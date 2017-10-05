class Bike(object):
    """docstring for Bike."""

    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def __str__(self):
        return "Bike: | Price: {} | Max Speed: {} | Miles: {} |".format(self.price, self.max_speed, self.miles)

    def displayInfo(self):
        print self
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing..."
        if self.miles >= 5:
            self.miles -= 5
        else:
            self.miles=0
        return self

bike1 = Bike("$200", "10mph")
bike2 = Bike("$500", "20mph")
bike3 = Bike("$800", "25mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
