class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
   
    def displayInfo(self):
        print "Price ($): " + str(self.price)
        print "Max Speed (mph): " + str(self.max_speed)
        print "Miles (mi): " + str(self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5

new_bike = Bike(10000, 120)
new_bike.ride()
new_bike.ride()
new_bike.ride()
new_bike.reverse()
new_bike.displayInfo()

new_bike2 = Bike(5000, 100)
new_bike2.ride()
new_bike2.ride()
new_bike2.reverse()
new_bike2.reverse()
new_bike2.displayInfo()

new_bike3 = Bike(20000, 150)
new_bike3.reverse()
new_bike3.reverse()
new_bike3.reverse()
new_bike3.displayInfo()