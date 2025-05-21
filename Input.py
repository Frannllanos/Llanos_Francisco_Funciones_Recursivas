from Validate import validar_numero

def get_int(mensaje:str, mensaje_error:str = "Error en el numero", minimo:int = 1, maximo:int = 10, reintentos:int = 3) -> int|None:
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
    return numero_entero

from Validate import validar_numero

def get_float(mensaje:str, mensaje_error:str = "Error en el numero", minimo:int = 1, maximo:int = 10, reintentos:int = 3) -> float|None:
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
    return numero_flotante

from Validate import validar_longitud

def get_string(mensaje:str, mensaje_error:str = "Error en la cadena", longitud_minima:int = 1, longitud_maxima:int = 10) -> str|None:
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
    return cadena
