#Crea una función llamada reducir_lista() que tome una lista como 
# argumento (crea también la variable lista_numeros), y devuelva la misma lista,
#  pero eliminando duplicados (dejando uno solo de los números si hay repetidos) 
# y eliminando el valor más alto. El orden de los elementos puede modificarse.

#Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

#Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por 
# la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el 
# resultado, sin imprimirlo.

def reducir_lista(lista):
    lista_numeros = list(set(lista)) # Elimina los duplicados convirtiendo la lista en un conjunto y luego de nuevo a una lista
    if lista_numeros: # Verifica si la lista sin duplicados no está vacía
        valor_mas_alto = max(lista_numeros) # Encuentra el valor más alto en la lista sin duplicados
        lista_numeros.remove(valor_mas_alto) # Elimina el valor más alto de la lista sin duplicados
    return lista_numeros # Devuelve la lista resultante sin duplicados y sin el valor más alto

def promedio(lista):
    if lista: # Verifica si la lista no está vacía para evitar división por cero
        return sum(lista) / len(lista) # Calcula y devuelve el promedio de los valores en la lista
    else:
        return 0 # Si la lista está vacía, devuelve 0 para evitar división por cero
    
# Ejemplo de uso
lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros) # Llama a la función reducir_lista con la lista_numeros para obtener la lista sin duplicados y sin el valor más alto
print(lista_reducida) # Imprime la lista reducida   
promedio_resultado = promedio(lista_reducida) # Llama a la función promedio con la lista reducida para calcular el promedio de los valores en la lista
print(promedio_resultado) # Imprime el resultado del promedio calculado
