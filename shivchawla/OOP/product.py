class Product(object):
    def __init__(self,price,itemname,weight,brand,cost,status = "for sale"):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def displayinfo(self):
        print "The price is:", self.price
        print "The item name is:", self.itemname
        print "The weight is:", self.weight 
        print "The brand is:", self.brand 
        print "The cost is:", self.cost 
        print "The status is:", self.status
        return self

    def sell(self):
        self.status = "sold"
        return self

    def addtax(self,tax):
        self.price += tax
        return self

    def returnproduct(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "in open box":
            self.status = "used"
            self.price = self.price * .8 #giving it a 20% discount
        return self #ALWAYS have a return self if you want to chain shit


testproduct1 = Product(10,"cheese",10,"Kraft",5)
testproduct1.addtax(1).sell().displayinfo()
