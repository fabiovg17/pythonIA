def suma(**kwargs):
    total = 0 # Inicializa una variable total en 0 para almacenar la suma de los valores de los argumentos
    for valor in kwargs.values(): # Recorre los valores de los argumentos proporcionados utilizando el método values() del diccionario kwargs
        total += valor # Agrega cada valor al total
    return total # Devuelve el resultado de la suma de los valores de los argumentos    

suma(a=1, b=2, c=3) # Llama a la función suma con los argumentos a=1, b=2 y c=3, devuelve 6
print(suma(a=1, b=2, c=3)) # Imprime el resultado de la función suma con los argumentos a=1, b=2 y c=3, que es 6

def multiplicar(**kwargs):
    total = 1 # Inicializa una variable total en 1 para almacenar el producto de los valores de los argumentos
    for clave, valor in kwargs.items(): # Recorre los valores de los argumentos proporcionados utilizando el método values() del diccionario kwargs
        print(f"Multiplicando {clave} con valor {valor}") # Imprime el nombre de la clave y su valor antes de multiplicar
        total *= valor # Multiplica cada valor al total utilizando el operador *=
    return total # Devuelve el resultado del producto de los valores de los argumentos

multiplicar(x=2, y=3, z=4) # Llama a la función multiplicar con los argumentos x=2, y=3 y z=4, devuelve 24
print(multiplicar(x=2, y=3, z=4)) # Imprime el resultado de la función multiplicar con los argumentos x=2, y=3 y z=


#uso de *args y **kwargs en la misma función, donde *args se utiliza para recibir una cantidad variable de argumentos posicionales, y **kwargs se utiliza para recibir una cantidad variable de argumentos con nombre (clave-valor). En este caso, la función ejemplo imprime los argumentos posicionales y los argumentos con nombre por separado.
def ejemplo(num1, num2, *args, **kwargs):
    print(f"Números posicionales: {num1}, {num2}") # Imprime los argumentos posicionales num1 y num2
    print(f"Argumentos adicionales (args): {args}") # Imprime los argumentos adicionales recibidos en *args
    print(f"Argumentos con nombre (kwargs): {kwargs}") # Imprime los argumentos con nombre recibidos en **kwargs        

ejemplo(1, 2, 3, 4, 5, a=6, b=7) # Llama a la función ejemplo con los argumentos posicionales 1 y 2, los argumentos adicionales 3, 4 y 5, y los argumentos con nombre a=6 y b=7     


# Tuplas y diccionarios como argumentos en funciones con *args y **kwargs
def procesar_datos(*args, **kwargs):
    print(f"Datos posicionales (args): {args}") # Imprime los datos posicionales recibidos en *args
    print(f"Datos con nombre (kwargs): {kwargs}") # Imprime los datos con nombre recibidos en **kwargs      

tupla_datos = [10, 20, 30] # Crea una tupla de datos
diccionario_datos = {'a': 1, 'b': 2, 'c': 3} # Crea un diccionario de datos
procesar_datos(*tupla_datos, **diccionario_datos) # Llama a la función procesar_datos utilizando el operador * para desempaquetar la tupla y