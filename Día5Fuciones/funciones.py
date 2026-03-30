def mi_funcion():
    print("Hola, esta es mi función")

def suma(a, b):
    return a + b    

#suma(3,4) # Llamada a la función suma con los argumentos 3 y 4, devuelve 7
print(suma(3,4)) # Imprime el resultado de la función suma con los argumentos 3 y 4, que es 7
mi_funcion() # Llamada a la función mi_funcion, imprime "Hola, esta es mi función"


def saludo():
    '''Esta función imprime un saludo personalizado'''


saludo() # Llamada a la función saludo, imprime el mensaje de saludo personalizado
print(saludo.__doc__) # Imprime la cadena de documentación de la función saludo,

def saludo_personalizado(nombre):
    '''Esta función imprime un saludo personalizado con el nombre proporcionado'''
    print(f"Hola, {nombre}! Bienvenido/a a la programación en Python.")

saludo_personalizado("Juan") # Llamada a la función saludo_personalizado con el argumento "Juan", imprime un saludo personalizado para Juan

nombre_persona = "Jakko"
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

un_numero = 5
def cuadrado(un_numero):
    return un_numero ** 2

