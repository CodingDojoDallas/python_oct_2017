class Product(object):
    """docstring for Product."""
    def __init__(self, name, price, weight, brand, cost, tax=0, status="for sale"):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.tax = tax
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self):
        self.price = self.tax * self.price + self.price
        return self

    def returned(self, returned):
        self.returned = returned
        if self.returned == "defective":
            self.status = "defective"
            self.price = 0
        elif self.returned == "used":
            self.status = "used"
            self.price = self.price - (self.price * .2)
        else:
            self.status = status

        return self
    def displayInfo(self):
        print "| Name: {} | Price (tax included): ${} | Weight: {}lbs | Brand: {} | Store Cost: ${} | Tax: {} | Sale Status: {} |".format(self.name, self.price, self.weight, self.brand, self.cost, self.tax, self.status)
        return self
product1 = Product("Snickers", 2, .5 , "Mars", .25, .1)
product2 = Product("M&Ms", 7, 1 , "Mars", 1.25, .1)


product1.addTax().sell().displayInfo()
product1.addTax().returned("used").displayInfo()
product2.addTax().returned("defective").displayInfo()
