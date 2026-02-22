
for numero in range(0, 16):
    print(f"El número es: {numero}")
    numero += 1


for numero in range(5):
    print(f"El número es: {numero}")
    numero += 1

#lectura de 5 a 10 (11 no incluido)
#el 2 indica que se salta de 2 en 2
for numero in range(10, 31, 2):
    print(f"El número es: {numero}")
    numero += 1

# Crear una lista de números del 1 al 20 usando range y convertirla en una lista
lista = list(range(1, 21))
print("Lista de números del 1 al 20:", lista)

mi_lista = list(range(2500, 2585))
print("Lista de números del 2500 al 2584:", mi_lista)

# calcular la suma de los cuadrados de los números del 1 al 15
suma_cuadrados = 0
for numero in range(1, 16):
    suma_cuadrados += numero ** 2   


print("La suma de los cuadrados de los números del 1 al 15 es:", suma_cuadrados)

    

