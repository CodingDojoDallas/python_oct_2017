class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax

    def display_all(self):
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        print "Price: $"+str(self.price)
        print "Speed: "+str(self.speed)+"mph"
        print "Fuel: "+self.fuel
        print "Mileage: "+str(self.mileage)+"mpg"
        print "Tax: "+str(self.tax)

car1 = Car(20000, 35, "Full", 25, 0)
car2 = Car(4000, 30, "Half", 30, 0)
car3 = Car(300000, 40, "Full", 20, 0)
car4 = Car(400, 20, "Empty", 10, 0)
car5 = Car(100, 10, "Full", 15, 0)
car6 = Car(20000, 50, "Full", 10, 0)
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
