# Zip
nombres = ['Ana', 'Luis', 'Carlos']
edades = [25, 30, 35]
ciudades = ['Madrid', 'Barcelona', 'Valencia']
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
# Crear una lista de tuplas combinando dos listas usando zip

# Listas de ejemplo
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']    
# Usar zip para combinar las listas
combinacion = list(zip(lista1, lista2))
print("Lista de tuplas combinadas:", combinacion)

# Desempaquetar valores de una lista de tuplas usando zip
tuplas = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*tuplas)
print("Números:", numeros)
print("Letras:", letras)    

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
concatendo = list(zip(capitales,paises))

for capitales, paises in (concatendo):
    print(f"La capital de {paises} es {capitales}")



num1 = ['uno', 'dos', 'tres','cuatro', 'cinco']
num2 = ['um', 'dois', 'três', 'quatro', 'cinco']
num3 = ['one', 'two', 'three', 'four', 'five']
combinacion_numeros = list(zip(num1, num2, num3))
print("Combinación de números en diferentes idiomas:", combinacion_numeros) 


