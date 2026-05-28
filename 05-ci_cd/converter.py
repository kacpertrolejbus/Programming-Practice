"""Funtion"""

def dec_to_bin(number):
    """Konwersja tu"""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Wartość naturalna")
    
    if not 0 <= number <= 100:
        raise ValueError("Liczba nie w przedziale")
    
    return bin(number)[2:]