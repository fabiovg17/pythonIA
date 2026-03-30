#Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros
#  que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    cantidad = len(kwargs) # Utiliza la función len para contar la cantidad de argumentos con nombre (clave-valor) recibidos en **kwargs
    return cantidad # Devuelve la cantidad de argumentos con nombre recibidos   

cantidad_atributos(a=1, b=2, c=3) # Llama a la función cantidad_atributos con los argumentos a=1, b=2 y c=3, devuelve 3
print(cantidad_atributos(a=1, b=2, c=3)) # Imprime el resultado de la función cantidad_atributos con los argumentos a=1, b=


#Crea una función llamada lista_atributos que devuelva en forma de lista los valores de 
# los atributos entregados en forma de palabras clave (keywords). La función debe preveer 
# recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    lista_valores = list(kwargs.values()) # Utiliza el método values() del diccionario kwargs para obtener los valores de los argumentos con nombre, y luego convierte ese resultado en una lista utilizando la función list()
    return lista_valores # Devuelve la lista de valores de los argumentos con nombre recibidos

lista_atributos(a=1, b=2, c=3) # Llama a la función lista_atributos con los argumentos a=1, b=2 y c=3, devuelve [1, 2, 3]
print(lista_atributos(a=1, b=2, c=3)) # Imprime el resultado de la función lista_atributos con los argumentos a=1, b=2



#Crea una función llamada describir_persona, que tome como parámetros su nombre y 
# luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

#Características de {nombre}:
#{nombre_argumento}: {valor_argumento}
#{nombre_argumento}: {valor_argumento}
#etc...
#Por ejemplo:

#describir_persona("María", color_ojos="azules", color_pelo="rubio")

#Mostrará en pantalla:

#Características de María:
#color_ojos: azules
#color_pelo: rubio
#No llames a la función, solamente definela sin llamarla.

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:") # Imprime el mensaje de introducción con el nombre de la persona
    for clave, valor in kwargs.items(): # Recorre los argumentos con nombre utilizando el método items() del diccionario kwargs para obtener tanto la clave como el valor de cada argumento
        print(f"{clave}: {valor}") # Imprime cada característica en formato "nombre_argumento: valor_argumento"     


describir_persona("María", color_ojos="azules", color_pelo="rubio") # Llama a la función describir_persona con el nombre "María" y los argumentos color_ojos="azules" y color_pelo="rubio", muestra las características de María en pantalla   
       