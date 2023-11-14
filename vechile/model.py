from abc import ABC, abstractmethod

# Define the abstract parent class 'Vehicle'
class vechile(ABC):
    def __init__(self, name, brands):
        self.name = name
        self.brands = brands



    @property
    @abstractmethod
    def Quantity(self):
        pass

    @abstractmethod
    def price(self):
        pass

       
