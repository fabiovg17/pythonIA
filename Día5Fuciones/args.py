# La función suma toma un número variable de argumentos y devuelve la suma de esos argumentos
# sin importar cuántos argumentos se le pasen. Utiliza un for para recorrer los argumentos y sumar cada uno al total, que se devuelve al final.
def suma(*args): 
    total = 0 # Inicializa una variable total en 0 para almacenar la suma de los argumentos
    for numero in args: # Recorre cada número en los argumentos proporcionados
        total += numero # Agrega cada número al total
    return total # Devuelve el resultado de la suma de los argumentos   



suma(1, 2, 3) # Llama a la función suma con los argumentos 1, 2 y 3, devuelve 6
print(suma(1, 2, 3)) # Imprime el resultado de la función suma con los argumentos 1, 2 y 3, que es 6        

def multiplicar(*args):
    total = 1 # Inicializa una variable total en 1 para almacenar el producto de los argumentos
    for numero in args: # Recorre cada número en los argumentos proporcionados
        total *= numero # Multiplica cada número al total
    return total # Devuelve el resultado del producto de los argumentos 

multiplicar(2, 3, 4) # Llama a la función multiplicar con los argumentos 2, 3 y 4, devuelve 24
print(multiplicar(2, 3, 4)) # Imprime el resultado de la función multiplicar con los argumentos 2, 3 y 4, que es 24


#otra forma mas sencilla de escribir la función suma utilizando la función sum incorporada de Python, que toma un iterable de números y devuelve la suma de esos números. En este caso, *args se pasa directamente a sum para obtener el resultado de la suma de los argumentos proporcionados.
def sumar(*args):
    return sum(args) # Utiliza la función sum para sumar todos los argumentos proporcionados y devuelve el resultado    

sumar(1, 2, 3) # Llama a la función sumar con los argumentos 1, 2 y 3, devuelve 6
print(sumar(1, 2, 3)) # Imprime el resultado de la función sumar con los argumentos 1, 2 y 3, que es 6

# lo que importa es el ***** args, el nombre de la variable es irrelevante, por lo que se puede usar cualquier nombre para la variable que almacena los argumentos variables. En este caso, se ha utilizado "variables" en lugar de "args", pero el funcionamiento de la función sigue siendo el mismo.
def sumarOtros(*variables): # se puede definir cualquiera PERO se recomienda usar ARGS!! por convención, ya que es el nombre comúnmente utilizado para representar argumentos variables en Python
    return sum(variables) # Utiliza la función sum para sumar todos los argumentos proporcionados y devuelve el resultado       

sumarOtros(4, 5, 6) # Llama a la función sumarOtros con los argumentos 4, 5 y 6, devuelve 15
print(sumarOtros(4, 5, 6)) # Imprime el resultado de la función sumarOtros con los argumentos 4, 5 y 6, que es 15