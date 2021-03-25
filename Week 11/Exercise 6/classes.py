class Product:
    def __init__(self,name, price, stock):
        self.name = name
        
        if price < 0:
            self.price = 0
        else:
            self.price = price
        
        if stock < 0:
            self.stock = 0
        else: self.stock = stock
        
    def name(self):
        return self.name

    def price(self):
        return self.price

    def stock(self):
        return self.stock    