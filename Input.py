from Validate import validar_numero

def get_int(mensaje:str, mensaje_error:str = "Error en el numero", minimo:int = 1, maximo:int = 10, reintentos:int = 3) -> int|None:
    """Ingresar int

    Args:
        mensaje (str): mensaje que pide el numero
        mensaje_error (str, optional): mensaje de error. Defaults to "Error en el numero".
        minimo (int, optional): numero minimo a pedir. Defaults to 1.
        maximo (int, optional): numero maximo a pedir. Defaults to 10.
        reintentos (int, optional): numero de reintentos. Defaults to 3.

    Returns:
        int|None
    """
    while reintentos > 0:
        try:
            numero_entero = int(input(mensaje))
            es_valido, mensaje_error_especifico = validar_numero(numero_entero, minimo, maximo)
            if es_valido:
                return numero_entero
            else:
                print(mensaje_error_especifico)
        except ValueError:
            print(mensaje_error)
        reintentos -= 1
    return None

from Validate import validar_numero

def get_float(mensaje:str, mensaje_error:str = "Error en el numero", minimo:int = 1, maximo:int = 10, reintentos:int = 3) -> float|None:
    """Ingresar flotante

    Args:
        mensaje (str): mensaje que pide el numero
        mensaje_error (str, optional): mensaje de error. Defaults to "Error en el numero".
        minimo (int, optional): numero minimo a pedir. Defaults to 1.
        maximo (int, optional): numero maximo a pedir. Defaults to 10.
        reintentos (int, optional): numero de reintentos. Defaults to 3.

    Returns:
        int|None
    """
    while reintentos > 0:
        try:
            numero_flotante = float(input(mensaje))
            es_valido, mensaje_error_especifico = validar_numero(numero_flotante, minimo, maximo)
            if es_valido:
                return numero_flotante
            else:
                print(mensaje_error_especifico)
        except ValueError:
            print(mensaje_error)
        reintentos -= 1
    return None

from Validate import validar_longitud

def get_string(mensaje:str, mensaje_error:str = "Error en la cadena", longitud_minima:int = 1, longitud_maxima:int = 10) -> str|None:
    """Pide una cadena

    Args:
        mensaje (str): mensaje que aparece en consola para pedir la cadena
        mensaje_error (str, optional): mensaje de error. Defaults to "Error en la cadena".
        longitud_minima (int, optional): longitud minima admitida. Defaults to 1.
        longitud_maxima (int, optional): longitud maxima admitida. Defaults to 10.

    Returns:
        str|None
    """
    while reintentos > 0:
        try:
            cadena = int(input(mensaje))
            es_valido, mensaje_error_especifico = validar_longitud(cadena, longitud_minima, longitud_maxima)
            if es_valido:
                return cadena
            else:
                print(mensaje_error_especifico)
        except ValueError:
            print(mensaje_error)
        reintentos -= 1
    return None
