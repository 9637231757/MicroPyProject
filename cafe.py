class Cafee:
    def __init__(self, name, price, quantity):
        self.product_name = name
        self.product_price = price
        self.quantity = quantity

    def __str__(self):
        return self.product_name + " , " + str(self.product_price) + " , " + str(self.quantity) + "\n"