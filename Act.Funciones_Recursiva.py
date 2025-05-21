from Input import get_int

#1
def sumar_naturales(numero:int) -> int:
    if numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)
#2
def calcular_potencia(base:int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente-1)
#3
def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero // 10)
#4
def calcular_fibonacci(numero:int) -> int:
    if numero == 0:
        return 0
    else:
        if numero == 1:
            return 1
        else:
            resultado = (calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2))
            return resultado

print(sumar_naturales(get_int("Introdusca un numero natural: ")))
print(calcular_potencia(get_int("Introdusca un numero como base: "), get_int("Introdusca otro numero como exponente: ")))
print(sumar_digitos(get_int("Introdusca un numero: ")))
print(calcular_fibonacci(get_int("Introdusca un numero para calcular fibonacci: ")))

