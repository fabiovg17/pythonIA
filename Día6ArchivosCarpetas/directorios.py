#abre directorios
import os
#Obtiene el directorio actual
directorio = os.getcwd()
print(directorio)

#otra forma de obtener el directorio actual
#directorio = os.path.dirname('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas')
ruta = directorio + '/' + 'Día6ArchivosCarpetas'
print(ruta)

#cambia el directorio actual a la ruta especificada
#ruta = os.chdir(directorio + '/' + 'Día6ArchivosCarpetas')
#print(os.getcwd())  

archivo = open('prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()

#crea un nuevo directorio
nuevo_directorio = ruta + '/' + 'NuevoDirectorio'
os.mkdir(nuevo_directorio) 

#elimina un directorio
os.rmdir(nuevo_directorio)
print(f"El directorio '{nuevo_directorio}' ha sido eliminado.") 
print(ruta)
#lista de archivos y carpetas en el directorio actual
#print(os.listdir(ruta))

# para obtener la ruta absoluta de un archivo o directorio
ruta_absoluta = os.path.abspath('prueba.txt')
print(ruta_absoluta)
# para obtener el nombre del archivo o directorio a partir de la ruta absoluta
elemento = os.path.basename(ruta_absoluta)
print(elemento)
#nombre del directorio padre a partir de la ruta absoluta
directorio_padre = os.path.dirname(ruta_absoluta)
print(directorio_padre)
#tubla para separar la ruta en partes
ruta_partes = os.path.split(ruta_absoluta)
print(ruta_partes)


#abrir un archivo utilizando la ruta absoluta
archivo = open('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas/prueba.txt')
print(archivo.read())   

# pathlib es una biblioteca que proporciona una forma más fácil y moderna de trabajar con rutas de archivos y directorios en Python. Permite manipular rutas de manera más intuitiva y ofrece una interfaz orientada a objetos para trabajar con archivos y directorios.
from pathlib import Path    # el Path va en mayúscula porque es un objeto de la biblioteca pathlib

carpeta = Path('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas')
print(carpeta)
archivo = carpeta / 'prueba.txt'  # para unir la ruta de la carpeta con el nombre del archivo
print(archivo)
print(archivo.read_text())  # para leer el contenido del archivo utilizando pathlib

#otra forma de abrir el archivo utilizando pathlib mas corta
carpeta2 = Path('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas') / 'prueba.txt'
mi_archivo = open(carpeta2)
print(mi_archivo.read())
#diferencia entre read y read_text es que read_text devuelve el contenido del archivo como una cadena de texto, mientras que read devuelve el contenido del archivo como un objeto de archivo que se puede leer línea por línea o en su totalidad.









