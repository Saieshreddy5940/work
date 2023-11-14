from vechile.truck import truck

# Test setup: create an instance of Biryani
Truck = truck("tiger", "layland", "Good")

# tests are written as functions that start with the word "test"
def test_truck_Quantity():
    # The assert statement checks for the result of a boolean expression
    # True means the test passed
    assert Truck.Quantity() == "It is used for goods"

def test_truck_price():
    assert Truck.price() == "It costs around $50000"

 

