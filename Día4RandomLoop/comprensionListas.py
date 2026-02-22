palabra = 'python'
 
lista = []

#recorrer cada letra de la palabra y agregarla a la lista
for letra in palabra:
    lista.append(letra)

print(lista)

# manera mas resumida
palabra = 'python'  
lista = [letra for letra in palabra]
print(lista)

# mas resumida aun
lista = [letra for letra in 'python']
print(lista)


# con rangos
numeros = [numero for numero in range(1, 11)]
print(numeros)  

#altearndo la lista
numeros = [numero * 2 for numero in range(1, 11)]
print(numeros)
# elevando al cuadrado cada numero
numeros = [numero ** 2 for numero in range(1, 11)]
print(numeros)      


# en el rango se indica que se va a leer del 1 al 10 (11 no incluido)
#el 3 indica que se va a leer de 3 en 3, es decir, se va a leer el 1, luego el 4, luego el 7 y luego el 10
numeros = [numero / 2 for numero in range(1, 11, 3)]
print(numeros)

##con condicionales
# if simple
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [valores for valores in valores if valores % 2 == 0]
print(valores_pares)

# en el rango se indica que se va a leer del 1 al 10 (11 no incluido)
# el if numero % 2 == 0 indica que se van a agregar a la lista solo los números pares, es decir, aquellos que al dividirlos por 2 no dejan residuo
numeros = [numero for numero in range(1, 11) if numero % 2 == 0]
print(numeros)

# condicionales con else    
# en este caso, se va a agregar a la lista el número si es par, pero si es impar se va a agregar el número multiplicado por 2, es decir, el número se va a duplicar
numeros = [numero if numero % 2 == 0 else numero * 2 for numero in range(1, 11)]
print(numeros)

# con condicionales anidados
# en este caso, se va a agregar a la lista el número si es par, pero si es impar se va a agregar el número multiplicado por 2, pero si el número es
# mayor que 5, se va a agregar el número multiplicado por 3, es decir, el número se va a triplicar
numeros = [numero if numero % 2 == 0 else numero * 2 if numero <= 5 else numero * 3 for numero in range(1, 11)]
print(numeros)

# multiplicando por 2 cada número del rango del 1 al 10, pero leyendo de 3 en 3, es decir, se va a leer el 1, luego el 4, luego el 7 y luego el 10
numeros = [numero * 2 for numero in range(1, 11, 3)]
print(numeros)

#otro else
# en este caso, se va a agregar a la lista el número multiplicado por 2 si el número multiplicado por 2 es mayor que 10, pero si el número multiplicado por 2 no es mayor que 10, se va a agregar la palabra 'no'
numeros = [numero if numero *  2 > 10 else 'no' for numero in range(1, 20,2)]
print(numeros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valores**2 for valores in valores]
print(valores_cuadrado) 

# uso cotidiano de las listas por comprensión
pies = [1, 2, 3, 4, 5]
metros = [pie * 0.3048 for pie in pies]
print(metros)


# obtiene grados Celcius a partir de una lista de grados Fahrenheit
fahrenheit = [32, 68, 100, 212]
celcius = [(temp - 32) * 5.0/9.0 for temp in fahrenheit]
print(celcius)