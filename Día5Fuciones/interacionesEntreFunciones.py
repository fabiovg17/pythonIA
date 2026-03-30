# importar librerias 
from random import shuffle 

#lista inicial
palitos = ['-', '--', '---', '----', '-----']


# mezclar palitos
def mezclar_palitos(lista):
    shuffle(lista) # Mezcla ale atoriamente los elementos de la lista palitos utilizando la función shuffle del módulo random
    return lista # Devuelve la lista mezclada de palitos

 
# pedir intento
def probar_suerte():
    intento =  ''  
    while intento not in ['1', '2', '3', '4', '5']: # Verifica si el intento ingresado por el usuario es válido (entre 1 y 5)
        intento = input("¿Cuál palito es el más corto? (1-5): ") # Solicita al usuario que ingrese su intento para adivinar cuál palito es el más corto
        if intento not in ['1', '2', '3', '4', '5']: # Si el intento ingresado no es válido, muestra un mensaje de error y solicita nuevamente el intento
            print("Intento inválido. Por favor, ingresa un número entre 1 y 5.")    

    return int(intento) # Devuelve el intento ingresado por el usuario


# compronbar intento  
def comprobar_intento(lista, intento):
    if lista[intento - 1] == '-': # Verifica si el palito seleccionado por el usuario (ajustando el índice para que coincida con la posición en la lista) es el más corto (representado por '-')
        print("¡Correcto! Has adivinado el palito más corto.") # Si es correcto, muestra un mensaje de felicitación
    else:
        print("Incorrecto. Inténtalo de nuevo.") # Si es incorrecto, muestra un mensaje de error

    print(f"Te ha tocado: {lista[intento-1]}") # Imprime el palito seleccionado por el usuario para mostrarle cuál ha sido su elección


# ejecutar el juego
palitos_mezclados = mezclar_palitos(palitos) # Mezcla los palitos utilizando la función mezclar_palitos y almacena el resultado en la variable palitos_mezclados
intento_usuario = probar_suerte() # Solicita al usuario que ingrese su intento utilizando la función probar_suerte y almacena el resultado en la variable intento_usuario
comprobar_intento(palitos_mezclados, intento_usuario) # Comprueba el intento del usuario utilizando la función comprobar_intento, pasando la lista de palitos mezclados y el intento del usuario como argumentos
