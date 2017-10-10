class Bike(object):
    def __init__(self, price, maxspeed):
        self.price = price
        self.maxspeed = maxspeed
        self.miles = 0

    def displayInfo(self):
        print "The price of this bike is " + str(self.price)
        print "The maximum speed is " + str(self.maxspeed)
        print "The mileage on this bike is " + str(self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        decrease = 5
        if(self.miles - decrease >= 0):
            self.miles -= decrease
        else:
            print "You went too far back!"
        return self


bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo() 

bike2 = Bike(50, "5mph")
bike2.ride().ride().reverse().reverse().displayInfo()    
   
bike3 = Bike(100, "15mph")
bike3.reverse().reverse().reverse().displayInfo()


