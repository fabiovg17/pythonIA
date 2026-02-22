# Ejemplo de uso de enumerate para obtener índices y valores de una lista
lista = ['manzana', 'banana', 'cereza']
for indice, valor in enumerate(lista):
    print(f"Índice: {indice}, Valor: {valor}")

# Ejemplo de uso de enumerate con un rango de números
for indice, valor in enumerate(range(5, 15)):
    print(f"Índice: {indice}, Valor: {valor}")


# Ejemplo de uso de enumerate con una cadena de texto
texto = "Hola"
for indice, caracter in enumerate(texto):
    print(f"Índice: {indice}, Carácter: {caracter}")    


# Ejemplo de uso de enumerate con una lista de tuplas
tuplas = [(1, 'a'), (2, 'b'), (3, 'c')]
for indice, (num, letra) in enumerate(tuplas):
    print(f"Índice: {indice}, Número: {num}, Letra: {letra}")   

lista = ['rojo', 'verde', 'azul']
mi_tupla = list(enumerate(lista))
print("Lista de tuplas con índices y valores:", mi_tupla)

for indice, valor in enumerate(lista):
    print(f"Índice: {indice}, Valor: {valor}")


lista_indices = "Python"

for indice, caracter in enumerate(lista_indices):
    print(f"indice: {indice}, caracter: {caracter}")
    
#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".
#Llama a la lista obtenida con el nombre de variable lista_indices 
lista_indices = list(enumerate("Python"))
print("Lista de índices y caracteres:", lista_indices)

#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:
#Loops
#Condicionales if
#El método enumerate()
#Métodos de strings o indexado

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(f"Índice: {indice}, Nombre: {nombre}")    
        