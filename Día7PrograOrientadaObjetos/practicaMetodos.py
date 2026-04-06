'''
Crea una clase Perro. Dicho perro debe poder ladrar.
Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, 
debe mostrarse en pantalla "Guau!".
'''

class Perro:
    def __init__(self):
        pass
    def ladrar(self):
        #return "Guau!"
        print("Guau!")  # se puede usar print para mostrar el mensaje en pantalla, aunque también se podría usar return para devolver el mensaje como resultado del método ladrar, pero en este caso se utiliza print para mostrar el mensaje directamente en pantalla.
perro1 = Perro()
print(perro1.ladrar())  # Guau!

'''
Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() 
(deberá imprimir "¡Abracadabra!").

Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
'''

class Mago:
    def __init__(self):
        pass
    def lanzar_hechizo(self):
        print("¡Abracadabra!")  # se puede usar print para mostrar el mensaje en pantalla, aunque también se podría usar return para devolver el mensaje como resultado del método lanzar_hechizo, pero en este caso se utiliza print para mostrar el mensaje directamente en pantalla.
merlin = Mago()
merlin.lanzar_hechizo()  # ¡Abracadabra!

'''
Crea una instancia de la clase Alarma, que tenga un método llamado 
postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"'''

class Alarma:
    def __init__(self):
        pass
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")  # se puede usar print para mostrar el mensaje en pantalla, aunque también se podría usar return para devolver el mensaje como resultado del método postergar, pero en este caso se utiliza print para mostrar el mensaje directamente en pantalla.
alarma1 = Alarma()
alarma1.postergar(10)  # La alarma ha sido pospuesta 10 minutos 



