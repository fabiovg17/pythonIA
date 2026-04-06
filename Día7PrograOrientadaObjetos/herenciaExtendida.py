#herencia Extendida

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite sonido")

class Pajaro(Animal):
    
    def __init__(self, edad, color, altura_vuelo):
        # una manera de crear nuevos atributos es declararlos todos como estos:
        # self.edad = edad
        #self.color = color
        # self.altura_vuelo = altura_vuelo
    # otra manera es el metodo super
        super().__init__(edad, color) # los reutilizo
        self.altura_vuelo = altura_vuelo #ese es nuevo


    # como este es el que llama la instacia entonces sobreescribe el hablar de la heredada
    def hablar(self):
        print("pio pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


piolin = Pajaro(2, 'Amarillo', 60) # al heredar lo de animal usa sus metodos como lo son el inicia y el nacer
print(piolin.color)
piolin.nacer()  # Hereda de la clase animal
piolin.hablar() 
piolin.volar(12)
mi_animal = Animal(5, "negro")
print(mi_animal.color)



