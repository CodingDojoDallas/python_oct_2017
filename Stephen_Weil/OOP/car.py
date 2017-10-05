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
        if __name__ == "__main__":
            self.display_all()
    
    def __repr__(self):
        return "<Car object - Mileage: {}>".format(self.mileage)
    
    def display_all(self):
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
        print "***********************"
        return self

if __name__ == "__main__":
    car1 = Car(2000, "60mph", "Full", "35mpg")
    car2 = Car(5000, "100mph", "Not Full", "25mpg")
    car3 = Car(15000, "130mph", "Full", "30mpg")
    car4 = Car(800, "50mph", "Not Full", "20mpg")
    car5 = Car(80000, "175mph", "Full", "35mpg")
    car6 = Car(1000, "60mph", "Not Full", "25mpg")