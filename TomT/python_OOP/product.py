#Assignment Product

class Product(object):
    def __init__(self, price, itemname, weight, brand, cost, status="for sale"):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def display_info(self):
        print self.price
        print self.itemname
        print self.weight
        print self.brand
        print self.cost
        print self.status
        print ""
        return self

    def sell(self):
        self.status = "sold"
        return self
        
    def AddTax(self, tax):
        self.price = round((tax*self.price),2)
        return self

    def Return(self, reason):
        if reason=="defective":
            self.status = "defective"
            self.price = 0
        elif reason=="returned in the box":
            self.status = "for sale"
        else:
            self.status = "used"
            self.price = self.price*.8
        return self

item1 = Product(3.99, "ketchup", "38oz", "Heinz", 3.00)

item1.display_info()

item1.AddTax(1.0825).display_info()

item1.Return("defective").display_info()