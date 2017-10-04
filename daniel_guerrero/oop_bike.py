# OOP Bike

# define the Bike class
"""
Create a new class called Bike with the following properties/attributes:

    price
    max_speed
    miles

Create 3 instances of the Bike class.

Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:

    displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
    ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
    reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
"""


class Bike(object):   # create a class bike and pass through the parameter the argument of object (letting it know its an object)
    def __init__(self, price, max_speed):  # __init__ is an initializer  of attributes
        self.price = price   
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):  # create a method called display info // have to pass self in the parameter
        print 'Price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles: ' + str(self.miles) + ' miles'

    def drive(self): # create a method called drive // have to pass self in the parameter
        print 'Driving'  # print driving
        self.miles += 10

    def reverse(self): # create a method called reverse // have to pass self in the parameter
        print 'Reversing'
        # prevent negative miles
        if self.miles >= 5:
            self.miles -= 5

# create instances and run methods
bike1 = Bike(99.99, 12)    # make an instance that is called bike 1 to run the bike method
bike1.drive()  # create an instance that is called bike 1 to run the bike method
bike1.drive()  # create an instance that is called bike 1 to run the bike method
bike1.drive()  # create an instance that is called bike 1 to run the bike methos
bike1.reverse() 
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.drive() # create an instance that is called bike 2 to run the drive method
bike2.drive() # create an instance that is called bike 2 to run the drive method 
bike2.reverse() # the reverse method will display whatver you want in reverse
bike2.reverse()
bike2.displayInfo()
