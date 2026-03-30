# recibe una palabra y devuelve una lista con las letras únicas de esa palabra, 
# ordenadas alfabéticamente.

def letras_unicas(palabra):
    letras = set()
    for letra in palabra:
        letras.add(letra)
   
    mi_lista = list(letras)
    mi_lista.sort()
    return (mi_lista)


letras_unicas("programacion") # Llamada a la función letras_unicas con el argumento "programacion", devuelve 9
print(letras_unicas("programacion")) # Imprime el resultado de la función letras_unicas con el argumento "programacion", que es 9