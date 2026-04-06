# Esto es un comentario de una sola línea
print("Hola, mundo")  # Esto también es un comentario

"""
Esto es un comentario
de varias líneas
usando comillas triples
"""

''' Practica 1
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home()
'''
from pathlib import Path
ruta_base = Path.home()
print(ruta_base)

'''
Implementa y crea una ruta relativa que nos permita llegar al archivo 
"practicas_path.py" a partir de la siguiente estructura de carpetas:

Curso Python -- dia 6 -- practicas_path.py
Almacena el directorio obtenido en la variable ruta. No olvides importar Path.

'''

ruta = Path("Curso Python", "dia 6", "practicas_path.py")
print(ruta)

'''
Implementa y crea una ruta absoluta que nos permita llegar al archivo
 "practicas_path.py" a partir de la siguiente estructura de carpetas:
 "Curso Python"
"Día 6"
"practicas_path.py"

Almacena el directorio obtenido en la variable ruta.
 No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta
   base del usuario.

'''
ruta_base = Path.home()
ruta = Path(ruta_base, "Curso Python", "Día 6", "practicas_path.py")
print(ruta)