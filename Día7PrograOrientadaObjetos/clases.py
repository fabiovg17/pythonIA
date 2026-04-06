#class
# las clases funcionan como plantillas para crear objetos, que son instancias de la clase. 
# Las clases pueden tener atributos (características) y métodos (comportamientos) que definen 
# el estado y el comportamiento de los objetos creados a partir de la clase.
# ayudan a organizar el código y a modelar el mundo real de manera más intuitiva,
#  permitiendo crear objetos con características y comportamientos específicos.

class Pajaro:
    # Atributos: nombre, color
    # Métodos: cantar(), volar()
    # el init es el método constructor que se ejecuta automáticamente al crear una instancia de la clase, se utiliza para inicializar los atributos de la clase.
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def cantar(self):
        return f"{self.nombre} está cantando."

    def volar(self):
        return f"{self.nombre} está volando."
    
pajaro1 = Pajaro("Piolín", "Amarillo")
print(pajaro1.cantar())
print(pajaro1.volar())  

otro_pajaro = Pajaro("Pájaro Loco", "Rojo")
print(otro_pajaro.cantar())
print(otro_pajaro.volar())  


# Atributos de clase: son compartidos por todas las instancias de la clase, se definen dentro de la clase pero fuera de cualquier método. Se accede a ellos a través de la clase o de una instancia.
class Perro:
    especie = "Canis lupus familiaris"  # Atributo de clase
    patas = True
    # Declaramos el método constructor __init__ para inicializar los atributos de instancia 
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo de instancia
        self.raza = raza      # Atributo de instancia

perro1 = Perro("Firulais", "Labrador")
perro2 = Perro("Rex", "Pastor Alemán")  
print(perro1.nombre)  # Firulais
print(perro1.raza)    # Labrador
print(perro1.especie) # Canis lupus familiaris
print(perro2.patas)   # True -- por medio de la instancia perro2 accedemos al atributo de clase patas, aunque también se puede acceder a través de la clase Perro.patas, pero es más común acceder a los atributos de clase a través de la clase.
print(Perro.patas)   # True // usa la clase para acceder al atributo de clase patas, aunque también se puede acceder a través de la instancia perro2.patas, pero es más común acceder a los atributos de clase a través de la clase.
print(perro2.nombre)  # Rex
print(perro2.raza)    # Pastor Alemán
print(perro2.especie) # Canis lupus familiaris



