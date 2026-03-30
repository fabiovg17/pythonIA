#Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
#La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
#Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente 
# los valores aleatorios.
# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
# (es decir, esta segunda función debe recibir dos argumentos) y que retorne 
# -sin imprimirlo- un mensaje según la suma de estos valores:
#Si la suma es menor o igual a 6:
#"La suma de tus dados es {suma_dados}. Lamentable"
#Si la suma es mayor a 6 y menor a 10:
#"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#Si la suma es mayor o igual a 10:
#"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
#Pistas: utiliza el método choice o randint de la biblioteca random 
# para elegir un valor al azar entre 1 y 6.

def lanzar_dados():
    import random # Importa la biblioteca random para generar números aleatorios
    dado1 = random.randint(1, 6) # Genera un número aleatorio entre 1 y 6 para el primer dado
    dado2 = random.randint(1, 6) # Genera un número aleatorio entre 1 y 6 para el segundo dado
    return dado1, dado2 # Devuelve los resultados de ambos dados como una tupla


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2 # Calcula la suma de los dos dados
    if suma_dados <= 6: # Verifica si la suma es menor o igual a 6
        return f"La suma de tus dados es {suma_dados}. Lamentable" # Retorna el mensaje correspondiente para esta condición
    elif 6 < suma_dados < 10: # Verifica si la suma es mayor a 6 y menor a 10
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances" # Retorna el mensaje correspondiente para esta condición
    else: # Si la suma es mayor o igual a 10
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora" # Retorna el mensaje correspondiente para esta condición
    
# Ejecutar el juego
dado1, dado2 = lanzar_dados() # Llama a la función lanzar_dados para obtener los resultados de ambos dados
resultado = evaluar_jugada(dado1, dado2) # Llama a la función evaluar_jugada con los resultados de ambos dados para obtener el mensaje
print(resultado) # Imprime el resultado de la evaluación de la jugada   