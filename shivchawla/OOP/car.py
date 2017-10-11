class Car(object): #this is declaring a class to take the God object
    def __init__(self,price,speed,fuel,mileage): #this is my init function that runs when created
        self.price = price #set self price to the price passed in
        self.speed = speed #set speed to the speed passed in
        self.fuel = fuel #set fuel to the fuel passed in
        self.mileage = mileage #set mileage to the mielage passed in
        if self.price > 10000: #if the price passed in is greater than 10k, set the tax to a value else a diff value
            self.tax = .15
        else:
            self.tax = .12
        self.display_all() #this is calling the other method that we created below
        
    
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        return self

car1 = Car(1000,20,"1gal",10000)
car2 = Car(1500,30,"2gal",10001)
car3 = Car(1700,40,"3gal",10002)
car4 = Car(1800,50,"4gal",10003)
car5 = Car(1900,60,"5gal",10004)
car6 = Car(2000,70,"6gal",10005)
