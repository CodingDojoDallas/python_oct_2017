class Car(object):
    """docstring for Car."""
    def __init__(self, price, speed, fuel, mileage, tax=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax

    def dispAll(self):
        print "Car: | Price: ${} | Max Speed: {}mph | Fuel: {}% | Mileage: {} | Tax: {}% |".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
        return self

    def taxCheck(self):
        if self.price <= 10000:
            self.tax += 12
        else:
            self.tax += 15
        return self

car1 = Car(4500, 110, 25, 200)
car2 = Car(10000, 120, 85, 250)
car3 = Car(12000, 110, 50, 300)
car4 = Car(35000, 130, 75, 350)
car5 = Car(80000, 185, 27, 350)
car6 = Car(250000, 200, 90, 300)
car1.taxCheck().dispAll()
car2.taxCheck().dispAll()
car3.taxCheck().dispAll()
car4.taxCheck().dispAll()
car5.taxCheck().dispAll()
car6.taxCheck().dispAll()
