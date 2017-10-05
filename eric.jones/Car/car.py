class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.displayall()

    def displayall(self):
        print "Price: {}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}\n".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(5000, "80mph", "Full", "15000mi")
car2 = Car(10000, "100mph", "3/4 Full", "10000mi")
car3 = Car(15000, "120mph", "1/2 Full", "20000mi")
car4 = Car(20000, "140mph", "1/4", "30000mi")
car5 = Car(25000, "160mph", "Almost Empty", "40000mi")
car6 = Car(30000, "180mph", "Fumes", "50000mi")