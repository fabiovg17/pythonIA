'''
Crees un código que le permita a 
una persona realizar operaciones en su cuenta bancaria.  
Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos: 
nombre y apellido. 
Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a 
heredar de Persona, porque los clientes son personas, por lo que el Cliente va a heredar 
entonces los atributos de Persona, pero también va a tener atributos propios, como número 
de cuenta y balance, es decir, el saldo que tiene en su cuenta bancaria.  

Pero eso no es todo: Cliente también va a tener tres métodos. El primero va a ser uno de los 
métodos especiales y es el que permite que podamos imprimir a nuestro cliente. 
Este método va a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos, 
incluyendo el balance de su cuenta. 
Luego, un método llamado Depositar, que le va a permitir decidir cuánto dinero quiere
 agregar a su cuenta. Y finalmente, un tercer método llamado 
Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta. 

Una vez que hayas creado estas dos clases, tienes que crear el código para que tu programa se 
desarrolle, pidiéndole al usuario que elija si quiere hacer depósitos o retiros. El usuario puede 
hacer tantas operaciones como quiera hasta que decida salir del programa. Por lo tanto, nuestro 
código tiene que ir llevando la cuenta de cuánto dinero hay en el balance, y debes procurar, por 
supuesto, que el cliente nunca pueda retirar más dinero del que posee. Esto no está permitido. 
Recuerda  que  ahora  que  sabes  crear  clases  y  objetos  que  son  estables  y  que  retienen 
información, no necesitas crear funciones que devuelvan el balance, ya que la instancia de 
cliente puede saber constantemente cuál es su saldo debido a que puede hacer sus operaciones 
llamando directamente a este atributo y no a una variable separada. 
Para que tu programa funcione, puedes organizar tu código como quieras, hay muchas formas 
de hacerlo, pero mi recomendación es que básicamente, 
luego de crear las dos clases que te he mencionado, crees dos funciones una que se 
encarguen de crear al cliente pidiéndole al usuario toda la información necesaria y 
devolviendo, a través del return, un objeto cliente ya creado. 

La otra función (que puede llamarse inicio, o algo por el estilo), es la función que 
organiza la ejecución de todo el código: primero llama a la función “crear cliente” y 
luego se encarga de mantener al usuario en un loop que le pregunte todo el tiempo 
si quiere depositar, retirar o salir 
del programa y demostrarle el balance, cada vez que haga una modificación. 

'''

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        #super permite llamar al método __init__ de la clase padre (Persona)
        # para inicializar los atributos nombre y apellido
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # defino para devolver los campos del cliente
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Número de cuenta: {self.numero_cuenta}, Balance: ${self.balance}"

    def Depositar(self, cantidad):
        self.balance += cantidad
        print(f"Has depositado ${cantidad}. Tu nuevo balance es: ${self.balance}")

    def Retirar(self, cantidad):
        #debe validar que tenga saldo:
        if cantidad > self.balance:
            print("No puedes retirar más dinero del que tienes en tu cuenta.")
        else:
            self.balance -= cantidad
            print(f"Has retirado ${cantidad}. Tu nuevo balance es: ${self.balance}")

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    #monto numerico con decimales
    balance = float(input("Ingrese su balance inicial: "))
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente

def inicio():
    # Referenciar la clase en cliente 
    cliente = crear_cliente()
    print(cliente)

    # el While se sale colo con el Break de Salir
    while True:
        accion = input("¿Qué acción deseas realizar? (Depositar/Retirar/Salir): ").lower()
        if accion == "depositar":
            cantidad = float(input("¿Cuánto deseas depositar?: "))
            cliente.Depositar(cantidad)
        elif accion == "retirar":
            cantidad = float(input("¿Cuánto deseas retirar?: "))
            cliente.Retirar(cantidad)
        elif accion == "salir":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige Depositar, Retirar o Salir.")

# llama al metodo inicial:
inicio()