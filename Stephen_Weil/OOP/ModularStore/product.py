class Product(object):

    def __init__(self, name, price, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
    def __repr__(self):
        return "<Product object - {}>".format(self.name)

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        return self.price + self.price*tax

    def take_back(self, reason):
        if reason == "defective":
            self.status = reason
            self.price = 0
        elif reason == "new":
            self.status = "for sale"
        elif reason == "used":
            self.status = reason
            self.price = self.price * .8
        else:
            print "Not a valid reason for return. Must be 'defective', 'new', or 'used'."
        return self
    
    def display_info(self):
        print self.name
        print "Price: $" + str(self.price)
        print "Weight: ", str(self.weight), "lbs"
        print "Brand: ", self.brand
        print "Cost: $" + str(self.cost)
        print "Status: ", self.status
        return self

if __name__ == "__main__":
    iphone = Product("iPhone", 800, .5, "Apple", 400)
    print "Price with tax: $" + str(iphone.add_tax(.1))
    iphone.display_info().sell().display_info().take_back('defective').display_info()
    samsung = Product("Galaxy S7", 500, .5, "Samsung", 250)
    print "Price with tax: $" + str(samsung.add_tax(.1))
    samsung.display_info().sell().display_info().take_back('used').display_info()
    nokia = Product("Old School Flip Phone", 50, 1, "Nokia", 10)
    print "Price with tax: $" + str(nokia.add_tax(.1))
    nokia.display_info().sell().display_info().take_back('new').display_info()