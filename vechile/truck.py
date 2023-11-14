from vechile.model import vechile

class truck(vechile):
    def __init__(self, name, brands, quality):
        super().__init__(name, brands)
        self.quality = quality

    def Quantity(self):
         return f"It is used for goods"

    def price(self):
         return f"It costs around $50000"
