import os
#leer un archivo
directorio = os.getcwd()
print(directorio)
#directorio = os.path.dirname('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas')
 
#Abre el archivo en modo lectura
archivo = open(directorio + '/' +'prueba.txt', 'r')

contenido = archivo.read()
print(contenido)



