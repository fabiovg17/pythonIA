
#from random import randint
from random import *

#generar un número aleatorio entre 1 y 100 con la función randint
aletorio = randint(1, 100)
print("Número aleatorio entre 1 y 100:", aletorio)  

#generar un número aleatorio entre 1.0 y 10.0 con la función uniform
aletorio = uniform(1.0, 10.0)
print("Número aleatorio entre 1.0 y 10.0:", aletorio)

#generar un número aleatorio entre 1.0 y 10.0 con la función uniform y redondearlo a dos decimales
aletorio = round(uniform(1.0, 10.0), 2)
print("Número aleatorio entre 1.0 y 10.0 con dos decimales:", aletorio) 

#generar un número aleatorio entre 0.0 y 1.0 con la función random
aletorio = random()
print("Número aleatorio entre 0.0 y 1.0:", aletorio)    

#forma directamente con la función choice
aletorio = choice(['manzana', 'banana', 'naranja'])
print("Fruta aleatoria:", aletorio) 

#lista que luego se obtiene un elemento aleatorio con la función choice
colores = ['rojo', 'verde', 'azul', 'amarillo']
aleatorio = choice(colores)
print("Colores aleatorios:", aleatorio) 

numeros = list(range(1, 11,2))
print("Números del 1 al 10:", numeros)

#mezclar la lista de números con la función shuffle
#numeros es una lista, por lo que se pasa directamente a la función shuffle
shuffle(numeros)
print("Números del 1 al 10 pero de 2 en 2 mezclados:", numeros)    

numeros = list(range(1, 11))
shuffle(numeros)
print("Números del 1 al 10 mezclados:", numeros)




