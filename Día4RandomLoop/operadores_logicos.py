
mi_bool = 4 < 5 <6 
print(mi_bool)  # True
mi_bool = 4 < 5 >6 
print(mi_bool)  # False
mi_bool = 4 < 5 and 5 < 6 
print(mi_bool)  # True
mi_bool = 4 < 5 and 5 > 6 
print(mi_bool)  # False
mi_bool = 4 < 5 or 5 > 6 
print(mi_bool)  # True
mi_bool = not(4 < 5 or 5 > 6) 
print(mi_bool)  # False

mi_bool = 4 < 5  and 8 > 7
print(mi_bool)  # False
mi_bool = (4 < 5  and 8 > 7) or (5 == 5)
print(mi_bool)  # True
mi_bool = ((4 < 5  and 8 > 7) or (5 == 5)) and (3 != 3)
print(mi_bool)  # False

texto = "esta es una cadena de texto"
mi_bool = "cadena" in texto
print(mi_bool)  # True

mi_bool =  not ("cadena" in texto)
print(mi_bool)  # False

mi_bool =  not "a" == "b"
print(mi_bool)  # True

