diccionario = {
    "hola": "hello",
    "adiós": "goodbye",
    "por favor": "please",
    "gracias": "thank you",
    "sí": "yes"}

print(diccionario["hola"])  # Accede al valor asociado a la clave "hola"

diccionario["buenos días"] = "good morning"  # Agrega un nuevo par clave-valor
print(diccionario)

diccionario["buenos días"] = "good morning222"  # Agrega un nuevo par clave-valor
print(diccionario)



resultado = diccionario["adiós"] # Accede al valor asociado a la clave "adiós"  
print(resultado)    

dic = {
    "nombre": "Juan",
    "edades": [12, 34, 56],
    "ciudad": "Madrid"
}
print(dic)
print(dic["edades"][1])  # Accede al segundo elemento de la lista asociada a la clave "edades"
print(dic ["edades"] )  # Accede a la lista completa asociada a la clave "edades"

listaListas = {
    "lista1": {"n1": "a",
               "n2": 2, 
                "n3": "c"},
    "lista2": [4, 5, 6],
    "lista3": [7, 8, 9]
}
print(listaListas["lista1"]["n2"])  # Accede al valor 2 dentro del diccionario en la lista1
print(listaListas["lista1"])  # Accede al diccionario completo asociado a la clave "lista1"
print(listaListas["lista1"]["n1"].upper())  # Accede al diccionario completo asociado a la clave "lista1"

print(listaListas.keys())  # Devuelve las claves del diccionario
print(listaListas.values())  # Devuelve los valores del diccionario
print(listaListas.items())  # Devuelve una lista de tuplas con las claves y valores del


mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])
# Accede al valor 300 dentro de la lista asociada a la clave "points2" en el diccionario "puntos"