archivo = open('texto.txt')
texto = archivo.read()
print(texto)


archivo = open('texto.txt')
texto = archivo.readline()
print(texto)

archivo = open('texto.txt')
texto = archivo.readline()
texto = archivo.readline()
print(texto)