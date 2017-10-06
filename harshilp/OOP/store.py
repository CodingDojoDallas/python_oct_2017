from product import *
class Store(object):
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = []

    def addProduct(self, product):
        self.products.append(product)
        return self

    def removeProduct(self, product):
        self.products.remove(product.name)
        return self
    
    def inventory(self):
        print "This store is located in " + self.location + " and owned by " + self.owner
        print "This store sells:"
        for prod in self.products:
            prod.displayInfo()
        return self

store = Store("Dallas", "HP")
toy = Product(100, "Stuffed toy", 2, "Build a bear")
lego = Product(130, "Lego set", 6, "Lego")
store.addProduct(toy)
store.addProduct(lego)
store.inventory()