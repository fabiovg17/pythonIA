#Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos 
# numéricos, y que retorne la suma de sus valores al cuadrado.

#Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

def suma_cuadrados(*args):
    total = 0 # Inicializa una variable total para almacenar la suma de los cuadrados
    for numero in args: # Itera sobre cada número en los argumentos proporcionados
        total += numero ** 2 # Agrega el cuadrado del número al total
    return total # Devuelve el resultado de la suma de los cuadrados

suma_cuadrados(1, 2, 3) # Llama a la función suma_cuadrados con los argumentos 1, 2 y 3, devuelve 14
print(suma_cuadrados(1, 2, 3)) # Imprime el resultado de la función suma_cuadrados con los argumentos 1, 2 y


#Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de 
# cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que 
# tome los valores sin signo y los sume, o lo que es lo mismo, los considere a 
# todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    total = 0 # Inicializa una variable total para almacenar la suma de los valores absolutos
    for numero in args: # Itera sobre cada número en los argumentos proporcionados
        total += abs(numero) # Agrega el valor absoluto del número al total utilizando la función abs()
    return total # Devuelve el resultado de la suma de los valores absolutos    

suma_absolutos(-1, 2, -3) # Llama a la función suma_absolutos con los argumentos -1, 2 y -3, devuelve 6
print(suma_absolutos(-1, 2, -3)) # Imprime el resultado de la función suma_absolutos con los argumentos -1, 2 y -3,


#Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre,
#  y a continuación, una cantidad indefinida de números.

#La función debe devolver el siguiente mensaje:

#"{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma_numeros = sum(args) # Calcula la suma de los números utilizando la función sum()
    return f"{nombre}, la suma de tus números es {suma_numeros}" # Devuelve el mensaje formateado con el nombre y la suma de los números        

numeros_persona("Juan", 1, 2, 3) # Llama a la función numeros_persona con el nombre "Juan" y los números 1, 2 y 3, devuelve "Juan, la suma de tus números es 6"
print(numeros_persona("Juan", 1, 2, 3)) # Imprime el resultado de la función numeros_persona con el nombre "Juan" y los números


