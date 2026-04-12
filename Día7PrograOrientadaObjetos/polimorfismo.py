# Polimorfismo 
# el polimorfismo es la capacidad de un objeto de tomar muchas formas, es decir, que un mismo método pueda funcionar con objetos de diferentes clases.

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Muuu")



class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

animales= [vaca1, oveja1]

#recorre las 2 instancias
#for animal in animales:
#    animal.hablar()

def animal_habla(animal):
    animal.hablar()
    
animal_habla(vaca1)
animal_habla(oveja1) 

#practica polimorfismo


