lista = ["manzana", "banana", "cereza"]
resultado = lista[1]  # Accediendo al segundo elemento  
print(resultado)

resultado = len(lista)  # Longitud de la lista
print(resultado)

lista[1] = "pera"  # Modificando el segundo elemento       
print(lista)
lista.append("naranja")  # Agregando un elemento al final de la lista
print(lista)
lista.pop()  # Eliminando el último elemento de la lista
print(lista)
lista.pop(0)  # Eliminando el último elemento de la lista
print(lista)

eliminado = lista.pop(0)  
print("Dato eliminado: " + eliminado)  # Guardando el elemento eliminado en una variable


otra_lista = list(("manzana", "banana", "cereza"))  # Usando el constructor de listas
print(otra_lista)
otra_lista.sort()  # Ordenando la lista
print(otra_lista)
otra_lista.reverse()  # Invirtiendo el orden de la lista
print(otra_lista)
print(type(lista))  # Devuelve el tipo de dato

resultado = otra_lista[-1:]  # Accediendo al último elemento
print(resultado)
print(type(resultado))  # Devuelve el tipo de dato

lista2 = ["kiwi", "naranja"]
print(lista + lista2)  # Concatenando listas

lista3 = lista + otra_lista + lista2  # Concatenando listas y guardando en una nueva
print(lista3)



