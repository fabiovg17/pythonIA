mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))  # Muestra el tipo de dato (list)
print(len(mi_set))  # Muestra la longitud del set (5)
print(mi_set)  # Muestra el contenido del set {1, 2, 3, 4, 5}
mi_set.add(6)  # Agrega el elemento 6 al set
print(mi_set)  # Muestra el contenido del set {1, 2, 3, 4, 5, 6}
mi_set.add(3)  # Intenta agregar el elemento 3 nuevamente (no se agrega porque ya existe)
print(mi_set)  # Muestra el contenido del set {1, 2, 3, 4, 5, 6}
mi_set.remove(2)  # Elimina el elemento 2 del set
print(mi_set)  # Muestra el contenido del set {1, 3, 4, 5, 6}
#mi_set.remove(10)  # Intenta eliminar el elemento 10 (genera un error porque no existe)
mi_set.discard(10)  # Intenta eliminar el elemento 10 (no genera error aunque no exista)
print(mi_set)  # Muestra el contenido del set {1, 3, 4, 5, 6}
print(3 in mi_set)  # Verifica si el elemento 3 está en el set (devuelve True)
print(10 in mi_set)  # Verifica si el elemento 10 está en el set (devuelve False)
sorteo = mi_set.pop()  # Elimina y devuelve un elemento aleatorio del set
print(sorteo)  # Muestra el contenido del set con un elemento menos
print(mi_set)  # Muestra el contenido del set con un elemento menos

lista = list(mi_set)  # Convierte el set en una lista
print(type(lista))  # Muestra el tipo de dato (list)
print(lista)  # Muestra el contenido de la lista [1, 3, 4, 5, 6] (el orden puede variar)
mi_set.clear()  # Elimina todos los elementos del set
print(mi_set)  # Muestra el contenido del set vacío set()
mi_set = {1, 2, 3, 4, 5}  # Otra forma de crear un set
print(mi_set)  # Muestra el contenido del set {1, 2, 3, 4, 5}       
mi_set2 = {4, 5, 6, 7, 8}
print(mi_set2)  # Muestra el contenido del set {4, 5, 6, 7, 8}       
print(mi_set.union(mi_set2))  # Unión de dos sets {1, 2, 3, 4, 5, 6, 7, 8}
print(mi_set.intersection(mi_set2))  # Intersección de dos sets {4, 5}
print(mi_set.difference(mi_set2))  # Diferencia de dos sets {1, 2, 3}
print(mi_set.symmetric_difference(mi_set2))  # Diferencia simétrica {1, 2, 3
set3 = set((1, 2, 3, (4, 5),6))  # Crea un set con una tupla como elemento
print(set3)  # Muestra el contenido del set {1, 2, 3, (4, 5)}       
# Los sets no pueden contener listas u otros sets