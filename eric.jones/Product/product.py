class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def displayinfo(self):
        print "Price: {}\nName: {}\nWeight: {}\nBrand: {}\nCost: {}\nStatus: {}\n".format(self.price, self.name, self.weight, self.brand, self.cost, self.status)
        return self

    def sell(self):
        self.status = "sold"
        return self

    def addtax(self, tax):
        self.price *= (1 + tax)
        return self

    def returnitem(self, reason):
        if reason == "defective":
            self.status = reason
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price *= .8
        return self

product = Product(50, "Airplane", "2lbs", "Mattel", "$15")
product.addtax(.08).sell().returnitem("opened").displayinfo()