
nombres = ["Ana", "Luis", "Carlos", "Marta"]
# Iterar sobre la lista de nombres
for nombre in nombres:
    numero_letras = len(nombre)
    print(f"El nombre {nombre} tiene {numero_letras} letras.")
    #determinar la posición del nombre en la lista
    numero_letra = nombres.index(nombre) + 1
    print(f"El nombre {nombre} es el número {numero_letra} en la lista.")

    print("Hola, " + nombre + "!")  
    if nombre.startswith("C"):
        print(f"El nombre {nombre} comienza con la letra C.")
    else:   
        print(f"El nombre {nombre} no comienza con la letra C.")
       

        

#lectura de 0 a 4 (5 no incluido)
for i in range(5):
    print("Número:", i) 

#lectura de 2 a 9 (10 no incluido)
for i in range(2, 10, 2):
    print("Número par:", i) 


# Sumar números en una lista usando un bucle for
numeros=[1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero
print("La suma de los números es:", suma)

for letra in "Python":
    print("Letra:", letra)
# Iterar sobre una lista de listas
for objeto in [[10,2], [23,34]]:
    print("Objeto:", objeto)
# Desempaquetar los valores directamente en el bucle
for a,b in [[10,2], [23,34]]:
    print("a:", a, "b:", b)

diccionario = {'x': 1, 'y': 2, 'z': 3}
for clave, valor in diccionario.items():
    print("Clave:", clave, "Valor:", valor) 

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementar el contador para evitar un bucle infinito

respuesta = 'S'
while respuesta == 'S':
    respuesta = input("¿Deseas continuar? (S/N): ").upper()
print("Has salido del bucle.")  

# Bucle infinito con break
while True:
    entrada = input("Escribe 'salir' para terminar el bucle: ")
    if entrada.lower() == 'salir':
        print("Saliendo del bucle.")
        break
    else:
        print("Has escrito:", entrada)

nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra.lower() == 'a':
        print("Se encontró la letra 'a', saliendo del bucle.")
        break
    print("Letra:", letra)

# Uso de continue
for numero in range(10):
    if numero % 2 == 0:
        continue  # Saltar los números pares
    print("Número impar:", numero)  



   