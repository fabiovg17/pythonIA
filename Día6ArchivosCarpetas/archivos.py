import os
#Obtiene el directorio actual
directorio = os.getcwd()
print(directorio)
#directorio = os.path.dirname('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas')
#Abre el archivo en modo lectura
archivo = open(directorio + '/' +'prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
una_linea = archivo.readline()
print(una_linea)
una_linea = archivo.readline()
print(una_linea.rstrip())
una_linea = archivo.readline()
print(una_linea)

archivo.close()


archivo = open(directorio + '/' +'prueba.txt', 'r')
for linea in archivo:
    print(linea.rstrip())
archivo.close()
#Abre el archivo en modo escritura
archivo = open(directorio + '/' +'prueba.txt', 'w')
archivo.write('Hola, este es un nuevo contenido')
archivo.close()
#Abre el archivo en modo lectura
archivo = open(directorio + '/' +'prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()

todas_las_lineas = ['Primera línea\n', 'Segunda línea\n', 'Tercera línea\n']
archivo = open(directorio + '/' +'prueba.txt', 'w')
archivo.writelines(todas_las_lineas)
archivo.close()
archivo = open(directorio + '/' +'prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()

archivo = open(directorio + '/' +'prueba.txt', 'r')
todas= archivo.readlines()
print(todas)
archivo.close()



