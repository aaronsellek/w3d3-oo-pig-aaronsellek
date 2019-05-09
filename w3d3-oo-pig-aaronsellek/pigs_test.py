from pigs.py import roll_die
    
def test_die():
    assert roll_die() in [1, 2, 3, 4, 5, 6]