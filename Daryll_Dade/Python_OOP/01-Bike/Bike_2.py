# Assignment: Bike
# Create a new class called Bike with the following properties/attributes:
#
# price
# max_speed
# miles
# Create 3 instances of the Bike class.
#
# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
#
# Add the following functions to this class:
#
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
#
# What would you do to prevent the instance from having negative miles?
#
# Which methods can return self in order to allow chaining methods?

class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        return self

    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self

    def riding(self):
        print self.miles + 10
        return self

    def reversing(self):
        if self.miles >= 5:
            self.miles - 5
        print self.miles
        return self

    def displayMiles(self):
        print "miles"
        return self


bike1 =Bike(200, 25)
bike2 =Bike(300, 30)
bike3=Bike(400, 45)

print "Bike Info: Price, Max Speed, Miles Ridden"
print "Bike 1"
bike1.displayInfo()
print "Bike 2"
bike2.displayInfo()
print "Bike 3"
bike3.displayInfo()

print "Riding:"
print "Bike 1 Ride 1"
bike1.riding().displayMiles()
print "Bike 1 Ride"
bike1.riding().riding().riding().reversing().displayInfo()
print "Bike 2 Ride"
bike2.riding().riding().reversing().reversing().displayInfo()
print "Bike 3 Ride"
bike3.reversing().reversing().reversing().displayInfo()
