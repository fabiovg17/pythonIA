'''mi_lista = [1, 1, 1, 1, 1]

print(len(mi_lista))

class Objeto:
    pass

objeto1 = Objeto()
print(objeto1)
'''

class CD:

    def __init__(self, autor, titulo,  canciones):
        self.titulo = titulo
        self.autor = autor  
        self.canciones = canciones

    #método especial para imprimir el objeto
    #cuando se llama a print() con una instancia de CD, se ejecuta este método
    # metodo str devuelve una representación legible del objeto, en este caso el título, autor y número de canciones del CD
    def __str__(self):
        return f"CD: {self.titulo} de {self.autor} con {self.canciones} canciones"

    # método especial para obtener la longitud del objeto, en este caso el número de canciones del CD
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print(f"El CD {self.titulo} ha sido eliminado")


mi_cd = CD("Metallica", "Master of Puppets", 8)
print(mi_cd)
print(len(mi_cd))
del mi_cd

#practica métodos especiales
'''
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se 
imprima el objeto, devuelva '"{titulo}", de {autor}' 
(atención: el título debe estar encerrado entre comillas dobles).

'''


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
    

'''
Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute 
la función len() sobre el mismo, devuelva el número de páginas como número entero.

'''

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas
    
'''
Dada la clase Libro, implementa el método especial __del__ para que el usuario sea
 informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro
   se elimine.

'''

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")