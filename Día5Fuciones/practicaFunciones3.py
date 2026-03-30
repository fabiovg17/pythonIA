#Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una 
# moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y 
# no debe recibir argumentos para funcionar.

#Crea una segunda función (llamada probar_suerte), que tome dos argumentos: 
# el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento,
#  será una lista de números cualquiera (debes crear una lista con valores y llamarla 
# lista_numeros).

#Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: 
# "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

#Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y 
# devolver la lista intacta.

#Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar
#  de una secuencia.

import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"]) # Utiliza la función choice de la biblioteca random para elegir al azar entre "Cara" y "Cruz"
    return resultado # Devuelve el resultado del lanzamiento de la moneda   

def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara": # Verifica si el resultado del lanzamiento de la moneda es "Cara"
        print("La lista se autodestruirá") # Si es así, imprime el mensaje de autodestrucción
        return [] # Devuelve una lista vacía para representar la destrucción de la lista original
    elif resultado_moneda == "Cruz": # Verifica si el resultado del lanzamiento de la moneda es "Cruz"
        print("La lista fue salvada") # Si es así, imprime el mensaje de salvación
        return lista_numeros # Devuelve la lista original intacta

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5] # Crea una lista de números
resultado_moneda = lanzar_moneda() # Llama a la función lanzar_moneda para obtener el resultado del lanzamiento de la moneda
resultado_final = probar_suerte(resultado_moneda, lista_numeros) # Llama a la función probar_suerte con el resultado del lanzamiento de la moneda y la lista de números, obtiene el resultado final
print(resultado_final) # Imprime el resultado final, que será una lista vacía si el resultado del lanzamiento de la moneda fue "Cara", o la lista original si el resultado fue "Cruz"

