
if 2 == 2:
    print("La condición es verdadera")  
elif 3 > 4:
    print("La condición es falsa")    
else:
    print("Ninguna de las condiciones anteriores se cumplió")   

numero = 7
numero2 = 10
if numero % 2 == 0:
    print(f"El número {numero} es par")
    if numero2 % 2 == 0:
        print(f"El número {numero2} es par")    
else:
    print(f"El número {numero} es impar")   
    if numero2 % 2 != 0:
        print(f"El número {numero2} es impar")
    else:
        print(f"El número {numero2} es par")


num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")


edad = 19
tiene_licencia = True

if edad >= 18:
    
    if not tiene_licencia:
        print("No puedes conducir. Necesitas contar con una licencia")
    else:
        print("Puedes conducir")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")













