class Bike(object):
    #the init method is called every time a new object is created
    def __init__(self,price,max_speed,miles = 0): #if you put a value to a parameter up here, it'll then set a default EVEN if shit isn't passed in
        #set some instance variables, just like any variable we can call these anything
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "This is my bike's price", self.price
        print "This is my bike's max speed", self.max_speed
        print "This is the miles rode on the bike", self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self #ALWAYS return self if your method doesn't return anything. OTHER than INIT
    def reverse(self):
        print "Reversing"
        if self.miles <=0: #this is so that you can't ever go below 0, restricting the ability to reverse from the start
            print "bro, you can't do that"
        else:
            self.miles -=5
        return self


mybike1 = Bike(100,24) #this sets "my bike" to have a price of 100 and a max speed of 24
#print mybike.displayinfo() #this is to call a method that was in your class. You must set an instance to call the method
mybike2 = Bike(150,25)
mybike3 = Bike(200,26)

mybike1.ride().ride().ride().reverse().displayinfo() #this is chaining. If you want to chain, return self in the method
mybike2.ride().ride().reverse().reverse().displayinfo()
mybike3.reverse().reverse().reverse().displayinfo()
