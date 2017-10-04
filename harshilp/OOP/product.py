class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price # active price/cost
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.cost = price  # stores the original price/cost
        self.displayInfo()

    def sell(self):
        self.status = "sold"
        return self

    def tax(self, amount):
        self.price = self.price + self.price*amount
        return self

    def returned(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
            self.price = self.cost
        else:
            self.status = "used"
            self.price = self.price*0.8
        return self
    
    def displayInfo(self):
        print "Price ($): " + str(self.price)
        print "Name: " + self.name
        print "Weight (lbs): " + str(self.weight)
        print "Brand: " + self.brand
        print "Status: " + self.status
        print "~~~~~~~~~~~~~~~~"
        return self

##testing
#toy = Product(100, "Stuffed toy", 2, "Build a bear")
#toy.tax(0.1)
#toy.sell()
#toy.returned("defective")
#toy.returned("in box")
#toy.returned("opened")
#toy.displayInfo()