def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("¡Hola!")
        funcion(palabra)
        print("¡Adiós!")
    return otra_funcion

#llama al decorador para decorar la función mayscula y minuscula

def mayuscula(texto):
    print(texto.upper())
    

def minuscula(texto):
    print(texto.lower())    

#decoramos las funciones mayuscula y minuscula con el decorador decorar_saludo
mayuscula_decorada = decorar_saludo(mayuscula)
minuscula_decorada = decorar_saludo(minuscula)
mayuscula_decorada("Hola Mundo") #esto imprimirá "¡Hola! HOLA MUNDO ¡Adiós!"
minuscula_decorada("Hola Mundo") 