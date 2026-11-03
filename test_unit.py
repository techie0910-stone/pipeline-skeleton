from app import apply_discount

def test_apply_discount_basic():
    assert apply_discount(10000, 0.2) == 8000
