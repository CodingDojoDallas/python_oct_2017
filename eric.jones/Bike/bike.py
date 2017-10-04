class Bike(object):

    def __init__(self, price, maxspeed):
        self.price = price
        self.maxspeed = maxspeed
        self.miles = 0

    def displayinfo(self):
        print "Price: {}  Maxspeed: {}  Miles: {}".format(self.price, self.maxspeed, self.miles)

    def ride(self):
        self.miles += 10
        return self

    def reverse(self):
        if self.miles > 4:
            self.miles -= 5
        return self

bike1 = Bike(500, "60mph")
bike2 = Bike(1200, "75mph")
bike3 = Bike(200, "35mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()