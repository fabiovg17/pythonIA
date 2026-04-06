# metodos en las clases

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
persona1 = Persona("Juan", 30)
print(persona1.saludar())  # Hola, mi nombre es Juan y tengo 30 años.

# ----- Metodos con parámetros -----
class Pajaro:
    def __init__(self, nombre, color, altura):
        self.nombre = nombre
        self.color = color
        self.altura = altura

    def cantar(self):
        return f"{self.nombre} está cantando."
    
    def piar(self):
        print('el color es {}'.format(self.color)) # el método piar es un método que muestra el color del pájaro, utilizando el atributo color de la clase Pajaro. El método piar no tiene parámetros, pero utiliza el atributo color para mostrar el color del pájaro.
        # el .format() es un método de las cadenas de texto que permite formatear una cadena con valores específicos, en este caso se utiliza para mostrar el color del pájaro en el mensaje.
    def volar(self, altura): # altura es un parámetro que se le pasa al método volar, y se puede utilizar dentro del método para mostrar la altura a la que está volando el pájaro.
        return f"{self.nombre} está volando a una altura de {altura} metros."
    
pajaro1 = Pajaro("Piolín", "Amarillo", 10)
print(pajaro1.cantar())  # Piolín está cantando.
print(pajaro1.volar(20))  # Piolín está volando.    -- cantidad de altura a la que vuela el pájaro, aunque en este caso no se está utilizando el parámetro altura dentro del método volar, pero se podría utilizar para mostrar la altura a la que está volando el pájaro. Por ejemplo: return f"{self.nombre} está volando a una altura de {altura} metros."
print(pajaro1.volar(pajaro1.altura))  # Piolín está volando a una altura de 10 metros. -- se le pasa el atributo altura del pájaro como parámetro al método volar, para mostrar la altura a la que está volando el pájaro.

pajaro1.piar()  # el color es Amarillo -- se llama al método piar para mostrar el color del pájaro, utilizando el atributo color de la clase Pajaro. El método piar no tiene parámetros, pero utiliza el atributo color para mostrar el color del pájaro. 