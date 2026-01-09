def es_palindromo(texto: str | None) -> bool:
    """
    Determina si un texto es un palíndromo ignorando espacios y mayúsculas.

    Reglas:
    - None -> False
    - No str -> TypeError
    - Ignora espacios y mayúsculas/minúsculas
    """
    if texto is None:
        return False

    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser una cadena (str) o None.")

    texto_limpio = texto.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]
