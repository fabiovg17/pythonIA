
def revisarNumero(numero):
    if numero < 0:
        return "El número es negativo"
    elif numero > 0:
        return "El número es positivo"
    else:
        return "El número es cero"
    
print(revisarNumero(-5)) # Llama a la función revisarNumero con el argumento -5, imprime "El número es negativo"
print(revisarNumero(10)) # Llama a la función revisarNumero con el argumento 10, imprime "El número es positivo"
print(revisarNumero(0)) # Llama a la función revisarNumero con el argumento 0, imprime "El número es cero"

def rango(numero):
   return numero in range(1, 11) # Devuelve un rango de números del 1 al 10 (excluyendo el 11)

print(rango(5)) # Llama a la función rango con el argumento 5, imprime el rango de números del 1 al 10   



#Rangos en Python, se pueden crear utilizando la función range() o utilizando la sintaxis de slicing en listas o cadenas.
def rango_nuevo(numero):
    return numero in range(10, 1100) # Devuelve un rango de números del 1 al 10 (excluyendo el 11)
    

suma = 123 + 456
resultado = rango_nuevo(suma) # Llama a la función rango_nuevo con el argumento suma, devuelve el rango de números del 10 al 1100
print(resultado) # Imprime el resultado de la función rango_nuevo con el argumento suma,


#For para recorrer una lista de números y verificar si cada número es de tres cifras o no.
def revisar_3_cifras(lista):
    for numero in lista:
        if numero in range(100, 1000): # Verifica si el número está en el rango de 100 a 999 (inclusive)
            return True
        else:
            pass

    return False # Si ningún número en la lista es de tres cifras, devuelve False    

numeros = [50, 9492, 1000, 1223]
revisar_3_cifras(numeros) # Llama a la función revisar_3_cifras con el argumento numeros, imprime si cada número en la lista es de tres cifras o no.
print(revisar_3_cifras(numeros)) # Imprime el resultado de la función revisar_3_cifras con el argumento numeros, que es True si al menos un número en la lista es de tres cifras, de lo contrario False




#Devuelve los números de tres cifras en una lista dada utilizando un for para recorrer la lista y verificar si cada número es de tres cifras o no.
def revisar_tres_cifras(lista):
    lista_tres_cifras = [] # Crea una lista vacía para almacenar los números de tres cifras encontrados
    for numero in lista:
        if numero in range(100, 1000): # Verifica si el número está en el rango de 100 a 999 (inclusive)
            lista_tres_cifras.append(numero) # Si el número es de tres cifras, lo agrega a la lista lista_tres_cifras
        else:
            pass

    return lista_tres_cifras # Devuelve la lista de números de tres cifras encontrados en la lista original

numeros = [50, 949, 1000, 123]
revisar_tres_cifras(numeros) # Llama a la función revisar_3_cifras con el argumento numeros, imprime si cada número en la lista es de tres cifras o no.
print(revisar_tres_cifras(numeros)) # Imprime el resultado de la función revisar_3_cifras con el argumento numeros, que es True si al menos un número en la lista es de tres cifras, de lo contrario False


#Crea una función (todos_positivos) 
#que reciba una lista de números como parámetro, y devuelva
#True si todos los valores de una lista son positivos, y 
#False si al menos uno de los valores es negativo. Crea una lista
#llamada lista_numeros con valores positivos y negativos.

def todos_positivos(lista):
    for numero in lista:
        if numero < 0: # Verifica si el número es negativo
            return False # Si encuentra un número negativo, devuelve False
    return True # Si todos los números son positivos, devuelve True
     
lista_numeros = [10, 20, -5, 30, 40] # Crea una lista de números con valores positivos y negativos
print(todos_positivos(lista_numeros)) # Llama a la función todos_positivos con el argumento lista_numeros, imprime True si todos los valores de la lista son





#Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

def suma_menores(lista):
    lista_numeros = 0 
    for n in lista:
        if n > 0 and n < 1000: # Verifica si el número es mayor a 0 y menor a 1000
            lista_numeros += n # Si el número cumple la condición, lo agrega a la suma total
    return lista_numeros # Devuelve el resultado de la suma de los números menores a 1000    

lista = [1, 2, 3, 4, 5] # Crea una lista de números
print(suma_menores(lista)) 




#Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
def cantidad_pares(lista):
    contador_pares = 0 # Inicializa un contador para los números pares
    for n in lista:
        if n % 2 == 0: # Verifica si el número es par (divisible por 2 sin residuo)
            contador_pares += 1 # Si el número es par, incrementa el contador
    return contador_pares # Devuelve la cantidad de números pares encontrados en la lista

lista_numeros = [1, 2, 3, 4, 5, 6] # Crea una lista de números
print(cantidad_pares(lista_numeros)) # Llama a la función cantidad_pares con el argumento lista_numeros, imprime la cantidad de números pares que existen en la lista,