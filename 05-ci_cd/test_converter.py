import pytest
from converter import dec_to_bin

def test_correct_conversion():
    """Testuje poprawność konwersji dla wartości skrajnych i środkowych."""
    assert dec_to_bin(0) == "0"
    assert dec_to_bin(5) == "101"
    assert dec_to_bin(100) == "1100100"

def test_out_of_range():
    """Testuje, czy podanie liczby spoza zakresu 0-100 rzuca ValueError."""
    with pytest.raises(ValueError):
        dec_to_bin(-1)
    with pytest.raises(ValueError):
        dec_to_bin(101)

def test_not_a_natural_number():
    """Testuje, czy podanie typu innego niż int rzuca TypeError."""
    with pytest.raises(TypeError):
        dec_to_bin(5.5)
    with pytest.raises(TypeError):
        dec_to_bin("10")