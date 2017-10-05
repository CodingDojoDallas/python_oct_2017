class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def __repr__(self):
        return "<Bike object, total mileage {}>".format(self.miles)
    
    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Max Speed: " + self.max_speed
        print "Total Miles: " + str(self.miles)
        return self

    def ride(self):
        print "Riding!"
        self.miles += 10
        return self

    def reverse(self):
        if self.miles >= 5:
            print "Reversing!"
            self.miles -= 5
        else: 
            print "You can't reverse! You haven't gone anywhere yet!"
        return self

if __name__ == "__main__":
    bike1 = Bike(200, "25mph")
    bike2 = Bike(300, "30mph")
    bike3 = Bike(100, "20mph")

    bike1.ride().ride().ride().reverse().displayInfo()
    bike2.ride().ride().reverse().reverse().displayInfo()
    bike3.reverse().reverse().reverse().displayInfo()