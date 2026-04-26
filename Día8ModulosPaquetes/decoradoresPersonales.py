
def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())
    
    def minuscula(texto):
        print(texto.lower())
        
    if tipo == "may":
            return mayuscula
        
    elif tipo == "min":
            return minuscula
#primero llamamos a la función para convertir a mayúsculas
operacion = cambiar_letras("may")
operacion("Hola Mundo") #esto imprimirá "HOLA MUNDO" 

operacion = cambiar_letras("min")
operacion("Hola Mundo")

