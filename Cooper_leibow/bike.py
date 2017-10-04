class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price, self.max_speed, self.miles

    def ride(self, times):
        print "riding"
        self.miles += (10 * times)
        print self.miles
        return self

    def reverse(self, times):
        print "reversing"
        self.miles -= (5 * times)
        print self.miles
        return self

bike1 = Bike("$100", "50mph", 100)
bike2 = Bike("$10000", "70mph", 1000)
bike3 = Bike("$1", "1000mph", 1)

bike1.ride(3).reverse(1).displayInfo()

bike2.ride(2).reverse(2).displayInfo()

bike3.reverse(3).displayInfo()
