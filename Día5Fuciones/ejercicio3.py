# saca si tiene un numere consecutivo repetido o no, devuelve True o False dependiendo del caso.
def ceros_vecinos(*args):
    contador = 0 # Inicializa un contador para los ceros vecinos

    for n in args: # Itera sobre cada número en los argumentos proporcionados

        if contador >= len(args) - 1: # Verifica si el contador ha alcanzado el penúltimo índice de los argumentos
           return False # Si el contador ha alcanzado el penúltimo índice, devuelve False porque no hay más números para comparar
        elif args[contador] == 0 and args[contador + 1] == 0: # Verifica si el número actual y el siguiente son ambos ceros
            return True # Si se encuentran dos ceros vecinos, devuelve True
        else:
            contador += 1 # Incrementa el contador para verificar el siguiente par de números

    return False # Si no se encuentran dos ceros vecinos, devuelve False


print(ceros_vecinos(1, 0, 0, 2, 3)) # Llama a la función ceros_vecinos con los argumentos 1, 0, 0, 2 y 3, imprime True porque hay dos ceros vecinos
print(ceros_vecinos(1, 0, 2, 0, 3)) # Llama a la función ceros_vecinos con los argumentos 1, 0, 2, 0 y 3, imprime False porque no hay dos ceros vecinos
print(ceros_vecinos(0, 1, 0, 2, 3)) # Llama a la función ceros_vecinos con los argumentos 0, 1, 0, 2 y 3, imprime False porque no hay dos ceros vecinos
print(ceros_vecinos(1, 2, 3, 4, 5)) # Llama a la función ceros_vecinos con los argumentos 1, 2, 3, 4 y 5, imprime False porque no hay dos ceros vecinos
print(ceros_vecinos(0, 0, 0, 0, 0)) # Llama a la función ceros_vecinos con los argumentos 0, 0, 0, 0  

