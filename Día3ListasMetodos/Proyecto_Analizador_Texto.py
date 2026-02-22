frase = input("Dime una frase: ")
frase = frase.lower()
Letras = input("Dime tres letras: ")
Letras = Letras.lower()
t = tuple(Letras)
if len(t) != 3:
    print("Error: Debes ingresar exactamente tres letras.")
    exit()

x, y, z = t  # Desempaquetado de la tupla en variables individuales
cantidadX = frase.count(x)
cantidadY = frase.count(y)
cantidadZ = frase.count(z)
print("\n")
print(f"la letra '{x}' aparece  {cantidadX}  Veces")  # Muestra los valores desempaquetados
print(f"la letra '{y}' aparece  {cantidadY}  Veces")  # Muestra los valores desempaquetados
print(f"la letra '{z}' aparece  {cantidadZ}  Veces")
print("\n")
print(f"El total de palabras en la frase es: {len(frase.split())}")
print("\n")
print(f"La primer letra es: {frase[0]}")
print(f"La ultima letra es: {frase[-1]}")
print("\n")
print(f"El texto invertido es: {frase[::-1]}")
print("\n")
print(f"Las palabras unidas sin espacios es: {frase.replace(' ', '')}")
print("\n")
VariableABuscar = "Python"
if VariableABuscar.lower() in frase:
    print(f"El texto contiene la palabra 'Python'") 
else:
    print(f"El texto no contiene la palabra 'Python'")




