nombre = "Carina "
#nombre[0] = "K"  #No se puede modificar un string, es inmutable
print(nombre * 3)

poema = '''
Rosas son rojas,
Violetas son azules,
El pasto es verde,
Y yo también.
'''
print(poema)  #Imprime el string tal cual
print("Rosas" in poema)  #Devuelve True si la palabra está en el string
print("Rosas" not in poema)  #Devuelve True si la palabra no está

print(len(poema))  #Devuelve la cantidad de caracteres del string, incluyendo espacios y saltos de línea

poema = '''Tierra mojada
mis recuerdos de viaje,
entre las lluvias'''

print("agua" not in poema)
