texto = "Este es un texto de prueba"
print(texto.upper())  # Convierte a mayúsculas
print(texto[2].upper())  # Convierte a mayúsculas lo que se encuentra en el índice 2
print(texto.lower())  # Convierte a minúsculas
print(texto.capitalize())  # Convierte la primera letra a mayúscula
print(texto.title())  # Convierte la primera letra de cada palabra a mayúscula
print(texto.strip())  # Elimina espacios al inicio y al final
print(texto.replace("prueba", "test"))  # Reemplaza una palabra por otra
print(texto.split(" "))  # Divide el texto en una lista de palabras
print(texto.split("t"))  # Divide el texto en una lista de palabras usando "t" como separador
print("-".join(texto.split(" ")))  # Une una lista de palabras en un texto
print(texto.find("prueba"))  # Busca una palabra y devuelve el índice de la primera letra
print(texto.count("e"))  # Cuenta cuántas veces aparece una
print(" ".join(texto))  # Une todos los caracteres del texto con un espacio entre ellos


