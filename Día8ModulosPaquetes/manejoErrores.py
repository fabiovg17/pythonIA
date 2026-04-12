def suma(): 
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    resultado = n1 + n2
    print(f"La suma de {n1} y {n2} es: {resultado}")
    #para el typeError:
    print("El resultado es: " + resultado) # Esto generará un TypeError porque resultado es un número, no una cadena.

    print("Gracias por usar la calculadora")


try:
    suma()
except ValueError:
    print("Error: Por favor, ingrese un número válido.")
except TypeError:
    print("Error: Tipo de dato no válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
else: ## Se ejecuta si no se produce ninguna excepción
    print("La operación se realizó correctamente.")

finally:
    print("Fin del programa.")
    

def pedir_numero():
    while True:
        try:
            numero = float(input("Ingrese un número: "))        
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            print("Intente nuevamente.")    
        else:
            print("Número ingresado correctamente.")
            break
    print(f"El número ingresado es: {numero}")  
      
numero = pedir_numero()
 
#practica
'''Hemos visto en la lección de qué manera se implementa el manejo
de errores habitualmente en Python. En el caso de este ejercicio, 
sin embargo, necesitaré que lo hagamos de una forma ligeramente 
distinta para que pueda ser evaluado: deberás implementarlo DENTRO 
de la función. En forma de comentario, verás un ejemplo de resolución.
Ten presente, sin embargo, que la forma preferida es la que hemos visto
en clase.

Implementa para la siguiente función suma(), un manejador de errores 
simple que ante cualquier error, imprima en pantalla el mensaje:
"Error inesperado". En caso contrario, deberá limitarse a mostrar
el resultado de la suma entre los dos números.'''

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def suma(num1,num2):
        
    try:
        print(num1+num2)
    except:
        print("Error inesperado")
        
suma(5,10) # Debería imprimir 15
suma(5,"10") # Debería imprimir "Error inesperado"


'''
Hemos visto en la lección de qué manera se implementa el manejo de
errores habitualmente en Python. En el caso de este ejercicio,
sin embargo, necesitaré que lo hagamos de una forma ligeramente
distinta para que pueda ser evaluado: deberás implementarlo DENTRO
de la función. En forma de comentario, verás un ejemplo de resolución. 
Ten presente, sin embargo, que la forma preferida es la que hemos visto
en clase.

Implementa para la siguiente función cociente(), un manejador
de errores:

Ante un error de tipo (TypeError), debe imprimir en pantalla
el mensaje: "Los argumentos a ingresar deben ser números"

Si se generara una división por cero (error del tipo ZeroDivisionError), 
el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"

En caso que no se produzca un error, deberá limitarse a imprimir el 
resultado del cociente (división) entre los dos números entregados como argumento.
'''

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

cociente(10,2) # Debería imprimir 5.0
cociente(10,"2") # Debería imprimir "Los argumentos a ingresar deben ser números"
cociente(10,0) # Debería imprimir "El segundo argumento no debe ser cero"    
#MENSAJE EN PANTALLA
"Los argumentos a ingresar deben ser números"
"El segundo argumento no debe ser cero"

'''
Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.

Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():

En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"

En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"

Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"

En todos los casos, al finalizar, imprimir: "Finalizando ejecución"

'''

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except Exception:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
    archivo = open(nombre_archivo)


#MENSAJES EN PANTALLA:
"El archivo no fue encontrado"
"Error desconocido"
"Abriendo exitosamente"
"Finalizando ejecución"
