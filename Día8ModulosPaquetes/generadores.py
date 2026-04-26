#funcion normal
def mi_funcion():
    return 2


#funcion generadora
def mi_funcion_generadora():
    yield 2 
    
#Ejemplo de resolución:
print(mi_funcion()) # Esto imprimirá 2
print(mi_funcion_generadora()) # Esto imprimirá un objeto generador
print(next(mi_funcion_generadora())) # Esto imprimirá 2


#------Listas------
# lista de numeros con generadores
def numeros():
    lista=[]
    for i in range(1,5):    
        lista.append(i * 10)
    return lista

def numeros_generadores():
    for i in range(1,5):
        yield i * 10
        
print(numeros()) # Esto imprimirá [10, 20, 30, 40]
print(numeros_generadores()) # Esto imprimirá un objeto generador

for numero in numeros_generadores():
    print(numero) # Esto imprimirá 10, 20, 30, 40, uno por línea


#--- con varios yields ---
def mi_generador():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x
    
for valor in mi_generador():
    print(valor) # Esto imprimirá 1, 2, 3, uno por línea    


#practica generadores
'''Crea un generador (almacenado en la variable generador) que sea capaz de devolver 
una secuencia infinita de números, iniciando desde el 1, y entregando un número
consecutivo superior cada vez que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio.'''

def generador_infinito():
    numero = 1
    while True:
        yield numero
        numero += 1
        
generador = generador_infinito()
print(next(generador)) # Esto imprimirá 1
print(next(generador)) # Esto imprimirá 2
print(next(generador)) # Esto imprimirá 3

'''Crea un generador (almacenado en la variable generador) que sea capaz de devolver de
manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea
llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).'''

def generador_multiplos_7():
    numero = 7
    while True:
        yield numero
        numero += 7

generador = generador_multiplos_7()
print(next(generador)) # Esto imprimirá 7
print(next(generador)) # Esto imprimirá 14
print(next(generador)) # Esto imprimirá 21

'''
Crea un generador que reste una a una las vidas de un personaje de videojuego, y 
devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida

'''
def generador_perder_vida():    
    vidas = 3
    while vidas > 0:
        yield f"Te quedan {vidas} vidas" if vidas > 1 else "Te queda 1 vida"
        vidas -= 1
    yield "Game Over"

perder_vida = generador_perder_vida()
print(next(perder_vida)) # Esto imprimirá "Te quedan 3 vidas"
print(next(perder_vida)) # Esto imprimirá "Te quedan 2 vidas"
print(next(perder_vida)) # Esto imprimirá "Te queda 1 vida"
print(next(perder_vida)) # Esto imprimirá "Game Over"