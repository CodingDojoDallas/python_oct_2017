class Product(object):
    def __init__(self, item_name, price, weight, brand, cost, status, return_box_status):
        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        self.return_box_status = return_box_status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.cost += (self.cost) * tax
        return self

    def Return(self, return_box_status):
        if self.return_box_status== "none":
            self.status = "defective"
            self.price = 0
        elif self.return_box_status == "open":
            self.status = "used"
            self.price *= .2
        return self

    def displayInfo(self):
        print self.item_name
        print self.price
        print self.weight
        print self.brand
        print self.cost
        print self.status
        print self.return_box_status

product1 = Product("Lettuce", 10, 3, "Green farms", 4, "for sale", "open")

product1.sell().displayInfo()
