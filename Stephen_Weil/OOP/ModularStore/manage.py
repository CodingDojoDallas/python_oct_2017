from product import Product
from store import Store

# name, price, weight, brand, cost

teddy_bear = Product("Teddy Bear", 20, .5, "FAO Schwartz", 2)
toy_soldiers = Product("Toy Soldiers", 1, .1, "Uncle Sam", .05)
nerf_gun = Product("Nerf Gun", 25, 2, "Nerf", 2.5)

myStore = Store("800 Imaginary Ave", "Stephen Weil")
print "Adding Three Toys and Displaying Inventory"
print "************"
myStore.info().add_product(teddy_bear).add_product(toy_soldiers).add_product(nerf_gun).inventory()
print "Sell Teddy Bear and Display It's Info"
print "************"
teddy_bear.sell().display_info()
print "Removing Teddy Bear and Displaying Inventory"
print "************"
myStore.remove_product(teddy_bear).inventory()
print "Taking Back Teddy Bear and Displaying Teddy Bear Info"
print "************"
teddy_bear.take_back('used').display_info()
print "Now Displaying Inventory With Teddy Bear"
print "************"
myStore.add_product(teddy_bear).inventory()
