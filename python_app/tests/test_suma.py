from python_app.utils import suma


# Pruebas para la función suma
def test_suma_positivos():
    assert suma(2, 3) == 5

def test_suma_cero():
    assert suma(5, 0) == 5

def test_suma_negativo():
    assert suma(-2, 3) == 1
