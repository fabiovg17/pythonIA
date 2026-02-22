mi_texto = "Esta es una prueba"
#Resultado = mi_texto[-4]  #trabaja con indices negativos
Resultado = mi_texto.index("n")  #trabaja con indices positivos
Resultado = mi_texto.index("a",5) #busca a partir del indice 5
#Resultado = mi_texto.index("a",5,11) #busca a partir del indice 5 y hasta el 10
#Resultado = mi_texto.index("prueba")  #busca la palabra y devuelve el indice del primer caracter
#Resultado = mi_texto.count("a")  #cuenta cuantas veces aparece el caracter
Resultado = mi_texto.rindex("a")  #busca de derecha a izquierda
print(Resultado)