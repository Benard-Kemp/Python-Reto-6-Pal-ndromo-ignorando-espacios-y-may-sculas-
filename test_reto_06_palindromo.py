import pytest
from reto_06_palindromo import es_palindromo


def test_palindromo_simple():
    assert es_palindromo("anilina") is True


def test_palindromo_con_mayusculas():
    assert es_palindromo("Anilina") is True


def test_palindromo_con_espacios():
    assert es_palindromo("anita lava la tina") is True


def test_no_palindromo():
    assert es_palindromo("hola mundo") is False


def test_cadena_vacia_es_palindromo():
    assert es_palindromo("") is True


def test_none_devuelve_false():
    assert es_palindromo(None) is False


def test_tipo_incorrecto_lanza_typeerror():
    with pytest.raises(TypeError):
        es_palindromo(123)
