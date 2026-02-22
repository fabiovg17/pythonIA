
x = 10
y = 5

print("Mis numeros son: " + str(x) + " y " + str(y)) # no es recomendable
print(f"Mis numeros son: {x} y {y}") #f string # recomendado

print("Mis numeros son: {} y {}".format(x,y)) # otra forma recomendada
print("La suma de: {} y {} es igual a {}" .format(x,y, x+y)) # Suma recomendada

#Mejor opción:
color = "rojo"
matricula = "ABC123"
print(f"El coche es de color {color} y su matricula es {matricula}")



puntos_anteriores = 875
puntos_nuevos = 350

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos")
                                                        
num1 = round(13/2,0)
print(f"El resultado de dividir 13/2 es {num1}")