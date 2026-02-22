texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = texto[2]  #El segundo indice no se incluye
fragmento = texto[2:5]  #El segundo indice no se incluye
fragmento = texto[2:10:2]  #El segundo indice no se incluye, el tercer indice es el salto
fragmento = texto[::-1]  #Invierte el texto
fragmento = texto[::-2]  #Invierte el texto de 2 en 2

print(fragmento)
