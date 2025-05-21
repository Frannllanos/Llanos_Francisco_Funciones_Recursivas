def validar_numero(numero:float, minimo:int = 1, maximo:int = 10) -> bool:
    """Valida si el numero es apto

    Args:
        numero (float): numero a validar
        minimo (int, optional): minimo de numeros. Defaults to 1.
        maximo (int, optional): maximo de numeros. Defaults to 10.

    Returns:
        bool: el booleano y el mensaje de error
    """
    if numero <= minimo:
        return False, f"Error: el numero debe ser mayor o igual a {minimo}"
    elif numero >= maximo:
        return False, f"Error: el numero debe ser menor o igual a {maximo}"
    else:
        return True, ""

def validar_longitud(cadena:str, minimo:int = 1, maximo:int = 10) -> bool:
    return minimo <= len(cadena) <= maximo