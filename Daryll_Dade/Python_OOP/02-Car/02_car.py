class Car(object):
    def __init__(self, price, speed, fuel, mileage):
         self.price = price
         self.speed = speed
         self.fuel = fuel
         self.mileage = mileage

    def tax(self):
        if self.price >10000:
            tax =.15
        else:
            tax=.10

    def display_all(self):
        print (self.price, self.speed, self.fuel, self.mileage, str(self.tax))

        # self.price = price
        #  self.speed = speed
        #  self.fuel = fuel
        #  self.mileage = mileage
        #  self.tax = tax

car1 =Car(2000, "35mph", "Full", "15mpg")
car2 =Car(2000, "5mph", "Not Full","105mpg")
car3 =Car(2000, "15mph", "Kind of Full", "95mpg")
car4 =Car(2000, "25mph", "Empty","25mpg")
car5 =Car(2000, "45mph", "Full", "25mpg")
car6 =Car(20000000, "15mph", "Full", "15mpg")

print "Car1"
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
