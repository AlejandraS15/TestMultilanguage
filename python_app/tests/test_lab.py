import pytest
from palindromo import es_palindromo
from utils import suma

# Pruebas para la función es_palindromo
def test_palindromo_radar():
    assert es_palindromo("radar") == True

def test_palindromo_anita_lava_la_tina():
    assert es_palindromo("anita lava la tina") == True

def test_palindromo_python():
    assert es_palindromo("python") == False

def test_palindromo_vacio():
    assert es_palindromo("") == True

def test_palindromo_radar_mayusculas():
    assert es_palindromo("Radar") == True


# Pruebas para la función suma
def test_suma_2_3():
    assert suma(2, 3) == 5

def test_suma_0_5():
    assert suma(0, 5) == 5

def test_suma_negativo_3():
    assert suma(-2, 3) == 1