from vechile.model import vechile

class car(vechile):
    def __init__(self, name, brands, color):
        super().__init__(name, brands)
        self.color = color

    def Quantity(self):
         return f"It is used for 4 to 6 people"

    def price(self):
         return f"It costs around $7000"