from random import *

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")

#con el while se repite el bloque de código mientras la condición sea verdadera, en este caso mientras los intentos sean menores a 8
while intentos < 8:
        #el dato viene en formato string, por lo que se convierte a entero con la función int para poder compararlo con el número secreto
        estimado = int(input("Cuál es el número?: "))
        intentos += 1

        if estimado < numero_secreto:
            print("Mi numero es mas alto")
        elif estimado > numero_secreto:
            print("Mi numero es mas bajo")
        else:
            print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
            break
#en caso de que se cumplan los 8 intentos sin adivinar el número secreto, se muestra un mensaje con el número secreto
if estimado != numero_secreto:
        print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")

