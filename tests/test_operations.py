from src.math_operations import add, sub, div, mul

# Testing the GitHub Actions CI Workflow

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-2, 3) == -6

def test_div():
    assert div(6, 3) == 2
    assert div(0, 5) == 0


