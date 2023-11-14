from vechile.car import car

Car = car("badsha", "tata", "red")

def test_Car_Quantity():
    assert Car.Quantity() == "It is used for 4 to 6 people"

def test_Car_price():
    assert Car.price() == "It costs around $7000"
