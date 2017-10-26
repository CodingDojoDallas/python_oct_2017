class Product(object):
    def __init__(self, price, ItemName, Weight, Brand, Cost, Status = "for sale"):
        self.price = price
        self.ItemName = ItemName
        self.Weight = Weight
        self.Brand = Brand
        self.Cost = Cost
        self.Status = Status
        

    def sell(self):
        self.Status = "sold"
        return self 
        

    def addTax(self, tax):
        self.price = round((self.price * self.tax),2)
        return self

    def returns(self, reason):
        if(reason == "defective"):
            self.Status = "Defective"
            self.price = 0

        elif(reason == "new"):
            self.Status = "for sale"
        
        else:
            self.Status = "used"
            self.price = self.price * .8
        return self

    def displayInfo(self):
        print self.price
        print self.ItemName
        print self.Weight
        print self.Brand
        print self.Cost
        print self.Status
        return self

product1 = Product(3.99, "Nail Polish", ".5 oz", "O.P.I", 12.5, "for sale")
product1.returns("used").displayInfo()

