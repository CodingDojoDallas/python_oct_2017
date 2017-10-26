class Item(object):
    def __init__(self, price, name, weight, brand, cost, status="for sale"):
        self.price = price
        self.name = name
        self.weight =weight
        self.brand = brand
        self.cost = cost
        self.status = status


    def sell(self):
        self.status = "sold"
        print self.status
        return self

    def tax(self, tax):
        self.price = self.price + self.price * tax
        print self.price


    def returned(self, reason):
        if reason == a1:
            print "return to manufacturer"
            self.price = 0
            print  self.price
        elif reason == a2:
            print a2, "like new.  discount 20%"
            self.price = self.price - self.price +.20
        elif  reason == a3:
            print  "used", self.price * .80
        else:
            print "Please enter approprate return reason"


a1 = "defective"
a2 = "like new"
a3 = "used"

x = Item(300, "watch", .5, "fosil", 200, "sold" )
print x.price
x.tax(.08)
x.sell()
x.returned(a3)
