# El Ahorcado. El juego es muy sencillo y popular, pero por si acaso te lo explico
# rápidamente.
# El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
# de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
# deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
# mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
# la palabra oculta, pierde una vida.
# En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo
# del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos
# gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una
# en una, cada vez que el jugador elija una letra incorrecta.
# Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra
# completa antes de perder todas las vidas, el jugador gana.
# Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas:
#  Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
# para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
# también vas a crear al comienzo.
#  Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
# haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
# ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
# palabra o no, para verificar si ha ganado o no, etc.
#  Recuerda escribir primero las funciones y luego el código que las implementa
# ordenadamente.
# Creo que este es un proyecto especial y de verdad quiero que sepas que no espero que lo puedas
# resolver sin ayuda. Las funciones parecen simples, pero cuando empezamos a poner funciones
# todas juntas en un código real, es difícil seguir mentalmente la sucesión del código porque se
# vuelve mucho menos lineal que antes. Lo importante es que lo intentes, que tu cabeza se
# zambulla en el problema y luego veremos cómo llegamos a la solución.

from random import choice

palabras = ["python", "programacion", "ahorcado", "funciones", "desarrollo"] # Crea una lista de palabras para el juego del ahorcado

letras_correctas = [] # Crea una lista vacía para almacenar las letras correctas adivinadas por el jugador
letras_incorrectas = [] # Crea una lista vacía para almacenar las letras incorrectas adivinadas por el jugador
intentos = 6 # Inicializa la cantidad de vidas del jugador 
aciertos = 0 # Inicializa un contador para los aciertos del jugador
juego_terminado = False # Inicializa una variable para controlar el estado del juego

def elegir_palabra(palabras):
    palabra_secreta = choice(palabras) # Utiliza la función choice para elegir una palabra al azar de la lista de palabras
    letras_unicas = len(set(palabra_secreta)) # Crea un conjunto de letras únicas en la palabra secreta para contar los aciertos necesarios para ganar
    return palabra_secreta,letras_unicas # Devuelve la palabra secreta elegida

def pedir_letra():
    letra_elegidas = ''
    es_valida = False
    abecedario = "abcdefghijklmnopqrstuvwxyz" # Define el abecedario para validar las letras ingresadas por el jugador
    while not es_valida: # Continúa pidiendo una letra hasta que el jugador ingrese una letra válida
        letra_elegidas = input("Elige una letra: ").lower() # Pide al jugador que ingrese una letra y la convierte a minúscula
        if letra_elegidas in abecedario and len(letra_elegidas) == 1: # Verifica si la letra ingresada es válida (está en el abecedario y es una sola letra)
            es_valida = True # Si la letra es válida, cambia el estado de es_valida a True para salir del ciclo
        else:
            print("Por favor, ingresa una letra válida (una sola letra del abecedario).") # Si la letra no es válida, muestra un mensaje de error y vuelve a pedir una letra

    return letra_elegidas # Devuelve la letra elegida por el jugador


def mostrar_nuevo_tablero(palabra_secreta):
    lista_oculta = [] # Crea una lista vacía para mostrar el estado actual del tablero con guiones y letras adivinadas
    for letra in palabra_secreta: # Recorre cada letra de la palabra secreta
        if letra in letras_correctas: # Verifica si la letra está en la lista de letras correctas adivinadas por el jugador
            lista_oculta.append(letra) # Si la letra es correcta, la agrega a la lista oculta para mostrarla en el tablero
        else:
            lista_oculta.append("_") # Si la letra no ha sido adivinada, agrega un guion a la lista oculta para representar una letra no adivinada
    print(" ".join(lista_oculta)) # Imprime el estado actual del tablero uniendo los elementos de la lista oculta con espacios

def verificar_letra(letra_elegida, palabra_secreta, vidas, coincidencias): 

    fin = False # Inicializa una variable para controlar si el juego ha terminado
    if letra_elegida in palabra_secreta and letra_elegida not in letras_correctas: # Verifica si la letra elegida por el jugador está en la palabra secreta
        letras_correctas.append(letra_elegida) # Si la letra es correcta, la agrega a la lista de letras correctas
        coincidencias += 1 # Incrementa el contador de coincidencias (aciertos)
    elif letra_elegida in letras_correctas or letra_elegida in letras_incorrectas: # Verifica si la letra elegida ya ha sido adivinada anteriormente (ya sea correcta o incorrecta)
        print("Ya has elegido esa letra antes. Por favor, elige una letra diferente.") # Si la letra ya ha sido adivinada, muestra un mensaje de advertencia para que el jugador elija una letra diferente
    else:
        letras_incorrectas.append(letra_elegida) # Si la letra es incorrecta, la agrega a la lista de letras incorrectas
        vidas -= 1 # Decrementa la cantidad de vidas del jugador    

    if vidas == 0: # Verifica si el jugador ha perdido todaes las vidas
        fin = perder() # Si es así, llama a la función perder para mostrar el mensaje de derrota y cambiar el estado de fin a True
    elif coincidencias == cantidad_letras: # Verifica si el jugador ha adivinado todas las letras únicas de la palabra secreta
        fin = ganar(palabra_secreta) # Si es así, llama a la función ganar para mostrar el mensaje de victoria y cambiar el estado de fin a True       
    
    return vidas, fin, coincidencias # Devuelve la cantidad de vidas restantes, el contador de coincidencias y el estado de fin del juego

def perder():
    print("¡Has perdido! La palabra secreta era:", palabra_secreta) # Muestra un mensaje de derrota y revela la palabra secreta
    return True # Devuelve True para indicar que el juego ha terminado

def ganar(palabra_secreta):
    mostrar_nuevo_tablero(palabra_secreta) # Muestra el tablero completo con la palabra secreta adivinada
    print("¡Felicidades, has ganado! La palabra secreta era:", palabra_secreta) # Muestra un mensaje de victoria y revela la palabra secreta
    return True # Devuelve True para indicar que el juego ha terminado

elegir_palabra(palabras) # Llama a la función elegir_palabra con la lista de palabras para obtener la palabra secreta y la cantidad de letras únicas
palabra_secreta, cantidad_letras = elegir_palabra(palabras) # Almacena la palabra secreta y la cantidad de letras únicas en variables para su uso posterior

while not juego_terminado: # Continúa el ciclo del juego mientras el juego no haya terminado
    print('\n' + '-'*20 + '\n') # Imprime una línea separadora para mejorar la visualización del juego
    mostrar_nuevo_tablero(palabra_secreta) # Muestra el estado actual del tablero con guiones y letras adivinadas
    print('\n') # Imprime una línea separadora para mejorar la visualización del juego
    print("Letras incorrectas:", " ".join(letras_incorrectas)) # Muestra las letras incorrectas adivinadas por el jugador
    print("Vidas restantes:", intentos) # Muestra la cantidad de vidas restantes del jugador
    print('\n' + '-'*20 + '\n') # Imprime una línea separadora para mejorar la visualización del juego
    letra_elegida = pedir_letra() # Llama a la función pedir_letra para obtener la letra elegida por el jugador
    intentos, juego_terminado, aciertos = verificar_letra(letra_elegida, palabra_secreta, intentos, aciertos) # Llama a la función verificar_letra para actualizar el estado del juego según la letra elegida por el jugador, obtiene la cantidad de vidas restantes, el contador de aciertos y
                                                          
    juego_terminado = juego_terminado # Actualiza el estado de juego_terminado con el valor devuelto por la función verificar_letra para controlar el ciclo del juego

