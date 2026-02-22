#las Tuplas consumen menos memoria que las listas
#las Tuplas son inmutables, no se pueden modificar, añadir o eliminar elementos una vez creadas
#las Tuplas se crean con paréntesis ()

tupla = (1, 2, 3, 4, 5)
print(tupla[0])  # Accede al primer elemento de la tupla
print(type(tupla))  # Muestra el tipo de dato (tupla)
print(len(tupla))  # Muestra la longitud de la tupla
print(tupla[-2])  # Accede al penúltimo elemento de la tupla
print(tupla[1:4])  # Accede a una porción de la tupla (del índice 1 al 3)


otra_tupla = ("a", "b", "c", "d")
print(otra_tupla)
print(otra_tupla + tupla)  # Concatenación de dos tuplas
print(otra_tupla * 2)  # Repetición de la tupla
print("b" in otra_tupla)  # Verifica si "b" está en la tupla (devuelve True o False)
print(otra_tupla.count("a"))  # Cuenta cuántas veces aparece "a" en la tupla
print(otra_tupla.index("c"))  # Devuelve el índice de la primera aparición de "c" en la tupla   
tupla_anidada = (1, 2, (3, 4), 5)
print(tupla_anidada[2])  # Accede a la sub-tupla (3, 4)
print(tupla_anidada[2][1])  # Accede al elemento 4 dentro de la sub-tupla   
#tupla[0] = 10  # Esto generará un error porque las tuplas son inmutables

tupla = list(tupla)  # Convierte la tupla en una lista
print(type(tupla))  # Muestra el tipo de dato (lista)
tupla[0] = 10  # Ahora se puede modificar el primer elemento
print(tupla)  # Muestra la lista modificada
tupla = tuple(tupla)  # Convierte la lista de nuevo en una tupla
print(type(tupla))  # Muestra el tipo de dato (tupla)
print(tupla)  # Muestra la tupla convertida

t = (1,2,3 )
x, y, z = t  # Desempaquetado de la tupla en variables individuales
print(x,y,z)  # Muestra los valores desempaquetados


