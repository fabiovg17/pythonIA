# decoradores
# metodos de instance: son los métodos que operan sobre una instancia específica de la clase, 
#       se definen con el primer parámetro self, que hace referencia a la instancia actual de 
#       la clase. 
#       Se accede a ellos a través de una instancia de la clase.  
# metodos de clase: son los métodos que operan sobre la clase en sí misma, se definen con el 
#       decorador @classmethod y el primer parámetro cls, que hace referencia a la clase. 
#       Se accede a ellos a través de la clase o de una instancia.
# metodos estaticos: son los métodos que no operan ni sobre la instancia ni sobre la clase, 
#       se definen con el decorador @staticmethod y no tienen un primer parámetro


class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio Pio")
        return f"El {self.especie} de color {self.color} está piando."
        
    
    def volar(self, metros):
        self.piar()
        return (f"El {self.especie} de color {self.color} está volando {metros}  metros")
        
    
    def pintar_negro(self):
        self.color =  'negro'
        print(f"Ahora el pajaro es {self.color}")

    # metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    #metodos Estaticos
    @staticmethod
    def mirar():
        print("El pajaro mira")


    
piolin = Pajaro("Amarillo", "Canario")
print(piolin.piar())  # El Canario de color Amarillo está piando.
print(piolin.volar(50))  # El Canario de color Amarillo está volando.
piolin.pintar_negro()
piolin.alas = False 
print(piolin.alas)

# metodos de clase, no requiere instanciarlo
Pajaro.poner_huevos(3)

# metoeods Estaticos, solo funcionan para devolver, no modifican
Pajaro.mirar()




class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre_mayuscula(self):
        return self.nombre.upper()

    @nombre_mayuscula.setter
    def nombre_mayuscula(self, nuevo_nombre):
        self.nombre = nuevo_nombre.lower()


persona = Persona("Juan", 30)
print(persona.nombre_mayuscula)  # JUAN
persona.nombre_mayuscula = "MARÍA"
print(persona.nombre)  # maría  

