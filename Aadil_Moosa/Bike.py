class Bike(object):
    def __init__ (self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Bike {}$ {}mph {}miles".format(self.price, self.max_speed, self.miles)
    
    def ride(self):
        print "Riding: {}".format(self.miles)
        self.miles = 10

    def reverse(self):
        print "Reversing: {}".format(self.miles)
        self.miles = 5

bike = Bike(200, 25)
bike.displayInfo()
bike.ride()
bike.reverse()

bike2 = Bike(250, 50)
bike2.displayInfo()
bike2.ride()
bike2.reverse()

bike3 = Bike(300, 75)
bike3.displayInfo()
bike3.ride()
bike3.reverse()
