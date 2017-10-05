class Car(object):
    def __init__ (self, price, speed, feul, mileage, tax):
        self.price = price
        self.speed = speed
        self.feul = feul
        self.mileage = mileage
        if price >= 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def displayAll(self):
        print "Price : {} bucks".format(self.price)
        print "Speed : {}mph".format(self.speed)
        print "Feul : {}".format(self.feul)
        print "Mileage : {}mpg".format(self.mileage)
        print "Tax : {}".format(self.tax)
        print "________________"

car1 = Car(2000, 35, "Full", 15, 0.12)
car1.displayAll()

car2 = Car(2000, 5, "Not full", 105, 0.12)
car2.displayAll()

car3 = Car(2000, 15, "Kind of full", 15, 0.12)
car3.displayAll()

car4 = Car(2000, 25, "Full", 15, 0.12)
car4.displayAll()

car5 = Car(2000, 45, "Empty", 15, 0.12)
car5.displayAll()

car6 = Car(20000000, 35, "Empty", 15, 0.15)
car6.displayAll()