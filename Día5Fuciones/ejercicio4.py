
#cuenta los numeros primos menores o iguales a un número dado (n) y devuelve el resultado de dicha cuenta.
def contar_primos(numero):
    primos = [2] # Crea una lista vacía para almacenar los números primos encontrados
    iterador = 3 # Inicializa un iterador para verificar los números a partir del 3

    if numero < 2: # Verifica si el número dado es menor que 2, en cuyo caso no hay números primos
        return 0 # Devuelve 0 porque no hay números primos menores o iguales a un número menor que 2
    
    while iterador <= numero: # Continúa verificando números hasta llegar al número dado
        for n in range(3, iterador, 2): # Verifica si el número actual es divisible por algún número impar menor que él
            if iterador % n == 0: # Si el número es divisible por algún número impar, no es primo
                iterador += 2 # Incrementa el iterador para verificar el siguiente número impar
                break # Rompe el ciclo para verificar el siguiente número impar
        else: # Si el número no es divisible por ningún número impar, es primo
            primos.append(iterador) # Agrega el número primo a la lista de primos
            iterador += 2 # Incrementa el iterador para verificar el siguiente número impar 

    print(primos) # Imprime la lista de números primos encontrados hasta el momento 
    return len(primos) # Devuelve la cantidad de números primos encontrados en la lista de primos

print(contar_primos(50)) # Llama a la función contar_primos con el argumento 10, imprime la cantidad de números primos menores o iguales a 10   


               