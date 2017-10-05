class Product(object):
    """docstring for Product."""
    def __init__(self, price, item_name, weight, brand, cost, status="for sale"):
        self.price = price
        self.item_weight = item_weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sold(self):
        self.status = "sold"

    def addTax(self, tax):
        self.tax = tax
        self.tax * self.price
        i dont know how I am currently doing this but I have the shittiest default finger placement on my keyboard ever. remember all of those shitty little typing programs as a kid in elementary school? Yea... I sucked ass at all of those and now look at me bro I am a mofokin genious 
