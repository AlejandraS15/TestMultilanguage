from python_app.palindromo import es_palindromo


# Pruebas para la función es_palindromo
def test_palindromo_radar():
    assert es_palindromo("radar")

def test_palindromo_anita_lava_la_tina():
    assert es_palindromo("anita lava la tina")

def test_palindromo_python():
    assert not es_palindromo("python")

def test_palindromo_vacio():
    assert es_palindromo("")

def test_palindromo_radar_mayusculas():
    assert es_palindromo("Radar")
