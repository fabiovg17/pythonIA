archivo = open('prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close() 


archivo = open('prueba.txt', 'w')
archivo.write('Hola, este es un nuevo contenido\n')
archivo.close() 
archivo = open('prueba.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close() 

archivo = open('prueba2.txt', 'a')
archivo.write('Hola, agregando una linea al final del archivo\n')
archivo.close() 
archivo = open('prueba2.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close() 

archivo = open('prueba3.txt', 'w')
archivo.writelines(['Primera línea\n', 'Segunda línea\n', 'Tercera línea\n'])
archivo.close() 

archivo = open('prueba3.txt', 'a')
lista = ['Cuarta línea', 'Quinta línea', 'Sexta línea']
for linea in lista:
    archivo.write(linea + '\n') 
    
archivo.close() 


archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo.close()
archivo = open('mi_archivo.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close() 

archivo = open('mi_archivo.txt', 'a')
archivo.write('Nuevo inicio de sesión')
archivo.close()
archivo = open('mi_archivo.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close() 

#Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

#registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

#Imprime el contenido completo de "registro.txt" al finalizar.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt', 'a')
archivo.writelines([elemento + '\t' for elemento in registro_ultima_sesion])
archivo.write('\n')
archivo.close()

