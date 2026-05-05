# Ejercicio 2 - Contar palabras en un archivo


def count_words(filename):
    """
    Lee un archivo y retorna un diccionario palabra -> cantidad.

    Reglas:
    - Las palabras se separan por espacios en blanco (cualquier tipo:
      espacios, tabs, saltos de línea). El método .split() sin argumentos
      ya maneja eso.
    - El conteo es case-insensitive: "Hola" y "hola" cuentan como la
      misma palabra. En el diccionario final las claves están en
      minúsculas.
    - Si el archivo está vacío, retornar {}.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, int] - cada palabra (en minúscula) con su frecuencia.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Hola mundo hola\nmundo python\n"
        count_words("texto.txt") -> {"hola": 2, "mundo": 2, "python": 1}
    """
    try:
        with open(filename, 'r') as archivo:
            contenido = archivo.read()
    except FileNotFoundError :
        raise FileNotFoundError

    dicc= contenido.split()
    res= {}

    for i in range(len(dicc)):
        clave = dicc[i]. lower()
        if clave in res:
            res[clave]+=1
        else:
            res[clave]= 1
    return res









