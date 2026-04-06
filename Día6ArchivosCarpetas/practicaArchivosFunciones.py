'''
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
y devuelva su contenido (read).
'''
import os
directorio = os.path.dirname('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas')
def abrir_leer(nombre_archivo):
    with open(directorio + '/' + nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

abrir_leer('prueba.txt')
print(abrir_leer('prueba.txt'))




'''
Crea una función llamada sobrescribir() que abra (open) 
un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior 
por el texto "contenido eliminado"

'''
import os
directorio = os.path.dirname('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas')

def sobrescribir(nombre_archivo):
    with open(directorio + '/' + nombre_archivo, 'w') as archivo:
        archivo.write('contenido eliminado')

sobrescribir('prueba.txt')
print(abrir_leer('prueba.txt'))


'''
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
Finalmente, debe cerrar el archivo abierto.
'''

import os
directorio = os.path.dirname('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas') 

def registro_error(nombre_archivo):
    
    with open(directorio + '/' + nombre_archivo, 'a') as archivo:
        archivo.write('se ha registrado un error de ejecución\n')   
        archivo.close()

registro_error('prueba.txt')
print(abrir_leer('prueba.txt'))

print("-------------------")
''' Esta es la solucion del profe'''
##Práctica Archivos y Funciones 1

def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()

#Práctica Archivos y Funciones 2

def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")

#Práctica Archivos y Funciones 3

def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()

