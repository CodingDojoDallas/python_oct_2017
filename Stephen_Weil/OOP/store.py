class Product(object):

    def __init__(self, name, price, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
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

class Store(object):
    
    def __init__(self, location, owner):
        self.products = {}
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        self.products[product] = product
        return self
    
    def remove_product(self, product):
        self.products.pop(product)
        return self

    def inventory(self):
        print "Displaying Inventory:"
        print "*********************"
        for product in self.products.values():
            product.display_info()
            print "*********************"
        return self

    def info(self):
        print "This store is located at", self.location
        print "This store is owned by", self.owner
        return self

iphone = Product("iPhone", 800, .5, "Apple", 400)
samsung = Product("Galaxy S7", 500, .5, "Samsung", 250)
nokia = Product("Old School Flip Phone", 50, 1, "Nokia", 10)

myStore = Store("800 Imaginary Ave", "Stephen Weil")
myStore.info().add_product(iphone).add_product(samsung).add_product(nokia).inventory()
myStore.remove_product(samsung).inventory()

otherStore = Store("1400 Different Place", "A Worse Owner")
otherStore.info().add_product(samsung).add_product(nokia).inventory()
otherStore.remove_product(nokia).inventory()