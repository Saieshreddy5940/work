from vechile.model import vechile

def test_vechile_is_abstract():
    try:
        vechile("bike", "ninja")
    except TypeError as e:
        assert "Can't instantiate abstract class vechile" in str(e)