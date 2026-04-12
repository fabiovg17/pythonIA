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
 
 