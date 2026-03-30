def sumar(a, b):
    return a + b

sumar(10, 20) # Llamada a la función sumar con los argumentos 10 y 20, devuelve 30
print(sumar(10, 20)) # Imprime el resultado de la función sumar con


def multiplicar(a, b):
    total = a * b
    return total


multiplicar(5, 4) # Llamada a la función multiplicar con los argumentos 5 y 4, devuelve 20
print(multiplicar(5, 4)) # Imprime el resultado de la función multiplicar con los argumentos 5 y 4, que es 20


def potencia(base, exponente):
    resultado = base ** exponente
    return resultado

potencia(2, 3) # Llamada a la función potencia con los argumentos 2 y 3, devuelve 8
print(potencia(2, 3)) # Imprime el resultado de la función potencia con los argumentos 2 y 3, que es 8

def invertir_palabra(palabra):
    return palabra[::-1].upper()    

invertir_palabra("Python") # Llamada a la función invertir_palabra con el argumento "Python", devuelve "nohtyP"
print(invertir_palabra("Python")) # Imprime el resultado de la función invertir_palabra con el argumento "Python", que es "nohtyP"